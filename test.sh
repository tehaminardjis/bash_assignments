#!/bin/bash

mkdir -p resultats

for fichier in *.csv; do
    [ -f "$fichier" ] || continue
    cp "$fichier" resultats/
done

echo "Les fichiers CSV ont été copiés avec succès."
