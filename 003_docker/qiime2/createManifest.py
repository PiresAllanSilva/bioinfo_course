#!/usr/bin/env python3

import os

from typing import List

def getFiles(path: str) -> List[str]:
    return os.listdir(path)

def generateNames(filename: str) -> str:
    return filename.split('_')[0]

def getDirection(filename: str) -> str:
    if '_R1_' in filename:
    	return 'forward'
    elif '_R2_' in filename:
    	return 'reverse'
    return 'unknown'

def generateManifest(names: List[str], files: List[str], directions: List[str], name: str = 'manifest.csv') -> None:
    with open(name, 'w') as manifest:
        manifest.write('sample-id,absolute-filepath,direction\n')
        for idx, name in enumerate(names):
            manifest.write(f'{name},/data/{files[idx]},{directions[idx]}\n')
    	        
if __name__ == '__main__':
    path = '/{path}/{to}/{data}' # Alter for your data location
    fastqFiles = getFiles(path=path)
    fastqFiles.sort()
    names = [generateNames(name) for name in fastqFiles]
    directions = [getDirection(direction) for direction in fastqFiles]
    generateManifest(names=names, files=fastqFiles, directions=directions)
