# Pipeline para realização das análises usando Qiime2

## Criação do Manifesto

```bash
python3 createManifest.py
```

## Instalação do rescript

[Github Rescript](https://github.com/bokulich-lab/RESCRIPt/)

[Fórum qiime](https://forum.qiime2.org/t/installing-community-plugins-in-docker/7106)

## Importação dos dados e conversão para artefato

```bash
mkdir output/
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  quay.io/qiime2/core:rescript qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path /data/manifest.csv \
  --output-path /output/rawreads.qza \
  --input-format PairedEndFastqManifestPhred33
```

## Importação do banco de referência

```bash
mkdir dbs/target_loci
cd dbs/target_loci
wget https://ftp.ncbi.nlm.nih.gov/refseq/TargetedLoci/Bacteria/bacteria.16SrRNA.fna.gz \
  -O 16S.gz
gunzip 16S.gz
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  quay.io/qiime2/core:rescript qiime tools import \
  --input-path /dbs/target_loci/16S \
  --output-path /dbs/target_loci/reference_sequences.qza \
  --type 'FeatureData[Sequence]'
```

## Visualização Dados Brutos

```bash
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  quay.io/qiime2/core:rescript qiime demux summarize \
  --i-data /output/rawreads.qza \
  --o-visualization /output/rawreads.qzv
```
 
## Remoção de primers (quando necessário)

```bash
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  quay.io/qiime2/core:rescript qiime cutadapt trim-paired \
   --i-demultiplexed-sequences /output/rawreads.qza \
   --p-cores 4 \
   --p-front-f TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGCCTACGGGNGGCWGCAG \
   --p-front-r GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGGACTACHVGGGTATCTAATCC \
   --p-discard-untrimmed \
   --p-no-indels \
   --o-trimmed-sequences /output/trimmedreads.qza
```

## Visualização Trimagem

```bash
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  quay.io/qiime2/core:rescript qiime demux summarize \
 --i-data /output/trimmedreads.qza \
 --o-visualization /output/trimmedreads.qzv
```

## Denoising (De (de = remoção) + noising (noise = ruído))

```bash
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  quay.io/qiime2/core:rescript qiime dada2 denoise-paired \
  --i-demultiplexed-seqs /output/trimmedreads.qza \
  --p-trunc-len-f 200 \
  --p-trunc-len-r 200 \
  --p-max-ee-f 2 \
  --p-n-threads 10 \
  --output-dir /output/DADA2
```

## Visualização Denoising

```bash
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  quay.io/qiime2/core:rescript qiime tools export \
  --input-path /output/DADA2/denoising_stats.qza \
  --output-path /output/DADA2/
```

```bash
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  quay.io/qiime2/core:rescript qiime feature-table summarize \
  --i-table /output/DADA2/table.qza \
  --o-visualization /output/DADA2/dada2_table_summary.qzv
```

## Criação dos bancos de dados

```bash
mkdir -p dbs/silva

docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime rescript get-silva-data \
  --p-version '138.1' \
  --p-target 'SSURef_NR99' \
  --p-include-species-labels \
  --p-rank-propagation \
  --o-silva-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs.qza \
  --o-silva-taxonomy /dbs/silva/silva-138.1-ssu-nr99-tax.qza

docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime rescript cull-seqs \
  --i-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs.qza \
  --o-clean-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs-cleaned.qza

docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime rescript filter-seqs-length-by-taxon \
    --i-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs-cleaned.qza \
    --i-taxonomy /dbs/silva/silva-138.1-ssu-nr99-tax.qza \
    --p-labels Archaea Bacteria Eukaryota \
    --p-min-lens 900 1200 1400 \
    --o-filtered-seqs /dbs/silva/silva-138.1-ssu-nr99-seqs-filt.qza \
    --o-discarded-seqs /dbs/silva/silva-138.1-ssu-nr99-seqs-discard.qza

docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime rescript dereplicate \
    --i-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs-filt.qza  \
    --i-taxa /dbs/silva/silva-138.1-ssu-nr99-tax.qza \
    # --p-rank-handles 'silva' \
    --p-mode 'uniq' \
    --o-dereplicated-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs-derep-uniq.qza \
    --o-dereplicated-taxa /dbs/silva/silva-138.1-ssu-nr99-tax-derep-uniq.qza

docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads  /dbs/silva/silva-138.1-ssu-nr99-seqs-derep-uniq.qza \
  --i-reference-taxonomy /dbs/silva/silva-138.1-ssu-nr99-tax-derep-uniq.qza \
  --o-classifier /dbs/silva/silva-138.1-ssu-nr99-classifier.qza

docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime feature-classifier extract-reads \
    --i-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs-derep-uniq.qza \
    --p-f-primer CCTAYGGGRBGCASCAG \
    --p-r-primer GGACTACNNGGGTATCTAAT \
    --p-n-jobs 2 \
    --p-read-orientation 'forward' \
    --o-reads /dbs/silva/silva-138.1-ssu-nr99-seqs-V3-V4.qza

docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime rescript dereplicate \
    --i-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs-V3-V4.qza \
    --i-taxa /dbs/silva/silva-138.1-ssu-nr99-tax-derep-uniq.qza \
    # --p-rank-handles 'silva' \
    --p-mode 'uniq' \
    --o-dereplicated-sequences /dbs/silva/silva-138.1-ssu-nr99-seqs-V3-V4-uniq.qza \
    --o-dereplicated-taxa  /dbs/silva/silva-138.1-ssu-nr99-tax-V3-V4-derep-uniq.qza
    
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime feature-classifier fit-classifier-naive-bayes \
    --i-reference-reads silva-138.1-ssu-nr99-seqs-V3-V4-uniq.qza \
    --i-reference-taxonomy silva-138.1-ssu-nr99-tax-V3-V4-derep-uniq.qza \
    --o-classifier silva-138.1-ssu-nr99-V3-V4-classifier.qza
```

OBS.: Essa etapa pode ser pulada, baixando-se o modelo treinado nesse [link](https://docs.qiime2.org/2023.7/data-resources/)

## Classificação Taxonômica

```bash
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime feature-classifier classify-sklearn \
   --i-reads /output/DADA2/representative_sequences.qza \
   --i-classifier /dbs/silva/silva-138-99-nb-classifier.qza \
   --p-n-jobs 2 \
   --output-path /output/SILVA/

docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime tools export \
   --input-path /output/SILVA/classification.qza \
   --output-path /output/SILVA/
```

# Visualização da tabela taxonomy.tsv

```bash
vim /output/SILVA/taxonomy.tsv
```

## Cross checking com Blast

```bash
docker run --rm \
  -v ${PWD}/data/:/data/ \
  -v ${PWD}/output/:/output/ \
  -v ${PWD}/dbs/:/dbs/ \
  quay.io/qiime2/core:rescript qiime feature-table tabulate-seqs \
  --i-data /output/DADA2/representative_sequences.qza \
  --o-visualization /output/DADA2/representative_sequences.qzv
```                                
































