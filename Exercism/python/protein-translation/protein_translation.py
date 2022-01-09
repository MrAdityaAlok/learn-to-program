def proteins(strand):
    codons = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
    }
    amino_acids = []
    splitted_strand = [strand[i : i + 3] for i in range(0, len(strand), 3)]
    for codon in splitted_strand:
        if codon in ("UAA", "UAG", "UGA"):
            break
        amino_acids.append(codons[codon])

    return amino_acids
