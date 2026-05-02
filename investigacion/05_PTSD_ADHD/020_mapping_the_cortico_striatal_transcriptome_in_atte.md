---
# Mapping the cortico-striatal transcriptome in attention deficit hyperactivity disorder
**Autores**: Gustavo Sudre
**Año**: 2022
**Journal**: Molecular Psychiatry, doi:10.1038/s41380-022-01844-9
**DOI/Link**: N/A

## Abstract
Not found

## Key Findings
DISCUSSION
The study has four central ﬁndings. First, we report signiﬁcant DEG
in the post-mortem ACC and to a lesser extent the caudate
nucleus
among
those
with
ADHD,
which
includes
genes
previously associated ADHD, other neuropsychiatric disorders,
and neuroplasticity. Secondly, DEGs in both the caudate and ACC
enriched gene sets associated with neurotransmitter activity, most
prominently glutamate, but also serotonin, GABA, and dopamine.
Third, in keeping with an inﬂuential developmental model of
ADHD [15–17], DEG in the caudate was most pronounced among
genes showing preferential early life expression in the caudate,
whereas DEG in the ACC was most prominently found in genes
expressed
in
adulthood.
Finally,
we
report
transdiagnostic
similarities in the post-mortem transcriptome between ADHD
and other neurodevelopmental and mood disorders, mirroring
their genetic overlap. The overall ﬁndings held when analyses
were
conﬁned
to
the
study’s
largest,
white,
non-Hispanic
subpopulation, a... (Extracted from Discussion)

## Methodology
METHODS
Clinical diagnoses
Psychiatric diagnosis was conducted by teams at each study site, through
DSM-based, clinician interviews with the next of kin and details are given
in the Supplementary Methods. Cases were deﬁned as those with a
diagnosis of any presentation of ADHD and the principal exclusion criteria
were the presence of any major neurological disorder or schizophrenia.
Controls were those determined to have no mental illness during the
diagnostic process. Twenty-six (12 cases and 14 controls) originated from
the National Institute of Mental Health Human Brain Collection Core
(HBCC) and 34 from the Neurobiobank (24 originated from the University
of Maryland Brain and Tissue Bank [10 cases and 14 controls], and ten
samples [5 cases and 5 controls] came from the Brain Tissue Donation
Program at the University of Pittsburgh). Procedures at the NIMH HBCC
procedures are approved by an oversight committee and the NIH
Department of Bioethics and all study sites acquired post-mortem tissue
and conducted all related procedures under protocols approved by their
local IRB. Details of the 60 subjects providing caudate and/or ACC samples
used in the ﬁnal analyses are given in Table 1 (for each region
Supplementary Table 1, and for brain bank differences Supplementary
Table 1C). Neither race/ethnicity (X2(2) = 4.3, p = 0.12), sex (X2(2) = 0.95,
p = 0.62), nor age at death (F(2, 57) = 1.6, p = 0.21) signiﬁcantly differed
among processing batches/brain banks. Following quality control proce-
dures, 49 provided both caudate and ACC tissue, four provided ACC only
and seven caudate only (Supplementary Fig. 1 shows quality control steps).
Tissue preparation
Brain tissues were dissected from frozen coronal slabs cut at autopsy. ACC
tissue was targeted anteriorly, above the genu of the corpus callosum, and
caudate tissue came from the head of the structure (see Supplementary
Fig. 2). Tissue was frozen at −80 °C and stored at −80 °C long-term. For
dissections, they were held in −80 °C and retrieved in small batches and
placed on dry ice, where all photography and dissections took place. Each
sample was on dry ice for ~30 min.
There were 60 donors. Sufﬁcient RNA was extracted for sequencing for
the ACC in 56 subjects and for the caudate in 59 subjects. Total RNA was
isolated from approximately 50–100 mg homogenized tissue in QIAzol
using QIAGEN RNeasy Lipid Tissue Mini Kit according to manufacturer
protocol. RNA Integrity Number (RINe) was analyzed using the Agilent
4200 TapeStation system and the Agilent RNA ScreenTape assay. RINe did
not differ by diagnosis (Supplementary Table 1), nor by brain bank of origin
(F(2, 106) = 1.2, p = 0.30).
RNA sequencing
RNA-seq was performed at the National Intramural Sequencing Center
using Illumina NovaSeq 6000, 2 × 150bp following Ribo-Zero GOLD
treatment to remove mitochondrial RNA and cytoplasmic rRNA. Samples
were sequenced in four batches with samples run in single lane within
each batch. The RNA-seq read mapping used STAR, an alignment software
package capable of mapping spliced RNA-seq reads to a genomic
reference sequence (GRCh38). Gencode gene annotations (V31) were used
as gene models during mapping of RNA-seq reads. The software package
QoRTs [22] was used to obtain quality control metrics from the RNA-seq
data. This included assessment of read quality (Phred quality scores),
nucleotide composition of sequence reads, and mapping quality of RNA-
seq reads. The software package RSEM was used to count the RNA-seq
data. After sequencing, one caudate sample was removed due to high
splice junction rate and outlying gene-body coverage metrics.
Differential gene expression
The gene expression data were subjected to principal components
analysis.
Visual
inspection
of
the
ﬁrst
two
principal
components
(Supplementary Fig. 3) revealed ﬁve outliers that were removed from
further analysis. The ﬁnal dataset was comprised of 53 ACC samples (24
ADHD and 29 unaffected) and 56 caudate samples (24 ADHD and 32
unaffected).
Gene read counts for ACC and Caudate were analyzed separately in R
(version 4.0.3). Genes with low expression were removed following Chen
Table 1.
Demographic and clinical details of the 60 donors.
ADHD
Unaffected
Test of group difference
Total
27
33
Age
Mean (SD; range)
21.3 (8.4;
6.7–38)
22.9 (8.0;
13.2–38.8)
t(55) = −0.078, p = 0.44
Sex
Male
23 (85.2%)
24 (72.7%)
X2(1) = 0.72, p = 0.40
Race/ethnicity
White (White Non-Hispanic)
21 (77.8%)
13 (39.4%)
X2(1) = 7.4, p = 0.006
Other
6 (22.2%)
20 (60.6%)
Evidence level
Conﬁrmed
15 (55.6%)
27 (81.8%)
X2(1) = 3.7, p = 0.054
Investigator impression
12 (44.4%)
6 (18.2%)
Comorbidities
Depression
8
NA
GAD/panic disorder
2
NA
Adjustment disorder
2
NA
Bipolar affective disorder
1
NA
Autistic spectrum disorder
1
NA
Substance use
No
14 (51.9%)
33 (100.0%)
Yes
13 (48.1%)”
NA
Manner of death
Accident
10
8
Exact p = 0.04
Natural
8
12
Homicide
1
9
Suicide
8
4
Post-mortem interval
Mean (SD; range) hours
27.3 (15.4;
7–69)
20.4 (10.5;
5–56.5)
t(44) = −1.99, p = 0.05
RINe
Mean (SD; range)
ACC: 5.2 (0.8; 4–6.7)
Caudate: 6.0 (0.5; 5.3–6.9)
ACC: 5.4 (0.7; 4–6.5)
Caudate: 5.9 (0.7; 4.5–7.1)
ACC: t(46) = −1.2, p = 0.22
Caudate: t(54) = 0.88, p = 0.38
Following quality control procedures, 49 provided both caudate and ACC tissue; 7 ACC only and 4 caudate only.
G. Sudre et al.
793
Molecular Psychiatry (2023) 28:792 – 800
et al. [23], implemented in function ﬁlterByExpr in edgeR (version 3.32).
DESeq2 (version 1.30.1) was used to estimate diagnostic differences in
gene expression, through negative binomial generalized linear models,
incorporating data-driven prior distributions in its estimates of dispersion
and logarithmic fold changes. Independent ﬁltering as implemented in
DESeq2, was also used to account for outliers in the data [24]. We
considered a range of variables that have been associated with gene
expression in prior studies: demographic/clinical features (age at death,
gender, comorbidities, mode of death, clinical evidence level), genotypic
(the ﬁrst ﬁve population components—C1 through C5), and technical
covariates (RNA-seq batch and brain bank of origin, post-mortem interval,
and RINe) for inclusion in the model (Supplementary Fig. 4). Group
differences among variables are listed in Supplementary Table 1. To select
the variables, we extracted the principal components of the gene
expression data and retained the components with eigenvalues above
one [25] (R package nFactors, version 2.4.1). The ﬁrst seven principal
components were retained for the ACC, accounting for 68% of variance,
and eight principal components were retained for the caudate, accounting
for 71% of variance. Spearman correlations tested for associations between
these principal components and continuous technical and demographic
covariates, while a Kruskal–Wallis test was used for categorical covariates.
Covariates associated with any principal component at a Bonferroni
corrected p value < 0.05 were retained in the ﬁnal model. For both ACC
and Caudate, RINe and brain bank/batch were selected. Finally, we also
included variables associated with diagnosis at a Bonferroni corrected p
value < 0.05, namely, the ﬁrst population component (C1), comorbidity,
and substance abuse. Detailed steps of analytical steps are provided in the
Supplementary Methods.
The full model used was thus:
geneExpression  C1 þ batch brain bank þ RINe þ comorbidity
þ substance abuse þ Diagnosis
where “C1” is the ﬁrst population component, derived from genotype data,
and “batch_brain_bank” is a variable indicating RNA-seq batch/brain bank
of origin. The coefﬁcient for “Diagnosis” determined the signiﬁcance of
each gene in differentiating ADHD from unaffected individuals. We also
report DESeq2’s posterior log2 fold changes, considered non-standardized
effect sizes that can be comparable across experiments [26].
Gene set enrichment analysis
Gene set enrichment analyses were conducted on the gene-level

## Results
results from
the DEG analysis, ranked using the sign of the log-fold change times the
negative log10(p value). We tested for enrichment of genes expressed in the
ACC and caudate across the lifespan and those conﬁned to different
developmental stages (prenatal, infant (0–2 years), child (3–11 years),
adolescent
(12–19
years),
and
adult
(>19
years).
These
gene
sets
(Supplementary Table 2) were derived from the Allen Brain Atlas to deﬁne
region-speciﬁc genes that are differentially expressed in the ACC but not in
the caudate, and vice-versa (package ABAEnrichment, version 1.20, quantile
cut-off 0.9, brain structures MFC_anterior/rostral cingulate or medial
prefrontal cortex—Allen:10278 and STR_striatum—Allen:10333). In these
analyses, the gene set enrichment test for each developmental stage is
independent; a statistical comparison across stages is not possible as
different genes are expressed at different developmental stages. However, a
normalized GSEA enrichment score can be determined for each develop-
mental stage, which allows a contrast of gene enrichment at each stage,
corrected for the number of genes expressed. The contrast of normalized
GSEA enrichment scores gives an impression of how ADHD-related change in
the transcriptome aligns with genes expressed at different stages, but should
not be interpreted as the results of direct, statistical contrasts.
Additionally, we tested for enrichment of non-redundant genes sets
deﬁned in Gene Ontology (http://www.geneontology.org) under the
domains of Biological Processes, Cellular Components, and Molecular
Functions using WebGestalt (R, version 0.4.4).
Transdiagnostic transcriptomic signatures
To contrast the transcriptome in ADHD against other disorder, transdiag-
nostic Spearman correlations were calculated between the absolute value
of the log-fold change in the post-mortem transcriptome of ADHD and the
transcriptome for other disorders, using 10,000 bootstraps (sampling with
replacement)–(for exact brain regions used for each diagnosis see
Supplementary Table 3). The p value was calculated against the null
distribution of studies of the same disorder.
Common variant risk for ADHD and gene expression
We tested the hypothesis that DEGs in ACC and caudate would overlap
with genes implicated in ADHD through GWAS. The 2019 Psychiatric
Genomics Consortium ADHD GWAS data release was used along with the
concatenation of European and African-American samples from 1000Gen-
omes as the reference data to estimate linkage disequilibrium between
SNPs [27]. These analyses used Multi-marker Analysis of GenoMic Annotation
(MAGMA) [28], which relates GWAS SNPs [18] to expressed genes by their
genomic positions. MAGMA then employs a SNP-wise sum model to test
mean SNP association to a gene-level continuous variable (the same gene
ranks used for GSEA). Reference data from the 1000Genomes project,
matching the speciﬁc GWAS populations being studied, were used for
linkage disequilibrium estimation used by MAGMA.
We also investigated whether DEGs for ADHD in ACC and caudate would
overlap with genes implicated through GWAS for other disorders,
speciﬁcally autistic spectrum disorders [29], major depression [30, 31],
bipolar affective disorder [32], schizophrenia [33], Tourette Syndrome [34],
obsessive compulsive disorder [35], post-traumatic stress disorder [36].
Finally, we used GSEA to ask whether copy-number variants in genes
previously implicated in ADHD would overlap with our differential
expression post-mortem results (list in Supplementary Table 4).
Genotyping
Genotyping was conducted on DNA extracted from brain tissue using the
Illumina
HumanOmniExpressExome-8v1–4
array
with
genome
build
GRCh38. Quality control measures are given in the Supplementary
Methods and 646,902 SNPs were retained for further analysis. Multi-
dimensional scaling in PLINK was used to characterize the population
structure (Supplementary Fig. 5) and the ﬁrst ﬁve dimensions were
retained in analyses.
Robustness analyses
We repeated analyses using different subgroups: the largest genotypic
subpopulation (white, non-Hispanic, deﬁned genotypically), and subjects
without major depressive disorders.
We also re-ran the analysis without entering comorbidity and substance
abuse as covariates, as these share genetic risk with ADHD, and controlling
for comorbidity could thus impact the detection of such shared genetic/
transcriptomic contributions. Finally, we also repeated the TWAS using a
leave-one-out cross validation approach, and report on the stability of the
association between ADHD and gene expression levels across the different
iterations. Data and code sharing information can be found in the
Supplementary Methods.
RESULTS
Cortico-striatal transcriptome proﬁling in ADHD
RNA sequencing was used to quantify gene expression in the caudate
and ACC, both key hubs in the cognitive control and attentional brain
systems that are disrupted in ADHD. We obtained an average of 109
million reads per sample (min 69, max 178, standard deviation 40) in
the ACC, detecting 24,945 genes and 17.1% unmapped reads. In the
caudate, there was an average 114 million reads per sample (min 76
million, max 196 million, SD 33) with 24,767 genes detected and
16.1% unmapped reads.
Fourteen genes showed signiﬁcant (FDR q < 0.05) diagnostic
differential expression of genes (DEG) in the ACC (Fig. 1 and
Supplementary File 1 [which include posterior log2 fold changes,
which are considered non-standardized effect sizes], and Supplemen-
tary Table 5). Twelve were protein coding and two were long non-
coding RNA; all showed upregulation in ADHD (Supplementary Fig. 6).
Two genes were previously implicated in ADHD (JPH2, Junctophilin
Type 2) [37] and alcohol dependence (KIAA0040, uncharacterized
protein) [38–40]. The differentially expressed gene ADAM-TS9 (A
Disintegrin-Like And Metalloprotease, Reprolysin Type, With Throm-
bospondin Type 1 Motif, 9), has been associated with a range of
neurocognitive features including white matter integrity in bipolar
disorder [41], neuroticism [42], brain surface area and subcortical
volume [43], and general cognitive ability [44]. Several genes are
involved in neuroplasticity: ANGPTL4 promotes angiogenesis and
neurogenesis in a mouse model of acute ischemic stroke, PDPN is
G. Sudre et al.
794
Molecular Psychiatry (2023) 28:792 – 800
involved in neural progenitor cells proliferation, and ADAMTS9
mediates synaptic plasticity, neurorepair [45–47].
The gene showing signiﬁcant differential expression in the
caudate (HILPDA, Hypoxia Inducible Lipid Droplet Associated) also
showed differential expression in the ACC. HILPDA has also been
found to be differentially expressed in the hippocampus of those
with major depressive disorder [48] and to be upregulated in
white matter lesions in multiple sclerosis [49].
Gene pathway analyses were performed to interrogate gene
expression differences beyond those attaining stringent levels of
signiﬁcance,
and
to
explore
possible
biological
effects
of
differentially expressed sets of genes. These analyses consistently
pointed to gene sets involved in neurotransmission. Using
Molecular Function Gene Ontology, DEGs in the caudate enriched
glutamate receptor genes, DEGs in the ACC implicated serotonin
and
GABA
receptor
activity,
and
the
broad
gene
set
of
neurotransmitter receptor activity was enriched by DEGs in both
regions (Fig. 2A and Supplementary File 1).
When examining sets in a Cellular Component Gene Ontology,
DEGs in the caudate also implicated processes pertaining to the
glutamatergic and GABAergic synapses, as well as synaptic processes
in general, and the neuronal spine (Fig. 2B and Supplementary Fig. 7
and Supplementary File 1 for full results). Semantic space analysis
(REVIGO) [50] highlighted the salient biological processes, including
post-synaptic specialization, the neuron spine, and glutamatergic
transmission (Supplementary Fig. 8).
Finally, GSEA results for Biological Processes largely followed a
similar pattern. DEGs in the caudate enriched gene sets related to
cognition, neuronal projection, dendritic development, synaptic
processes, as well as glutamate and dopamine receptor signaling
pathways (Supplementary File 1). ACC signiﬁcant results (FDR
q < 0.05) included serotonin receptor signaling pathway. The
results of a leave-one-out cross validation approach in the main
association analyses are given in Supplementary Table 6, and
point to stability in the results across the different iterations.
DEGs and genes expressed at different developmental stages
A prediction stemming from a leading developmental model of
ADHD is that caudate DEGs would preferentially enrich genes
preferentially expressed in the prenatal/infantile caudate, whereas
0.0
2.5
5.0
7.5
10.0
−2
0
2
4
 log2 fold change
 −log10 (p)
ACC
0.0
2.5
5.0
7.5
10.0
−2
0
2
4
 log2 fold change
Caudate
A
PDPN
KIAA
KIAA
I
KIAA
KIAA
KI A0040
0040
0040
04
0040
40
CCDC
CCDC
CCDC
CCD
CCDC
CCDC
CCD 13
13
13
ADAMTS
AMTS
AMTS9
MYO1G
O1G
O1G
Y
HILPDA
ENSG
ENSG0000
00000240
0240758
758
CRIS
CRIS
RI PLD1
PLD1
ENSG
ENSG
ENSG0000
0000
00000286
0286
0286922
922
922
CCL2
CCL2
CCL2
ANGP
ANGP
ANGPTL4
TL4
TL4
HAMP
AM
AM
AM
AM
AM
AM
AM
ZNF256
JPH2
0.0
2.5
5.0
7.5
10.0
1
2
3
4
5
6
7
8
9
10
11
12
13 14 15 16
18
20 22
 −log10 (p)
ACC
HILPDA
0.0
2.5
5.0
7.5
10.0
1
2
3
4
5
6
7
8
9
10
11
12
13 14 15 16
18
20 22
Chromosome
 −log10 (p)
Caudate
B
Fig. 1
Differential gene expression results. A Volcano plots for ACC and Caudate. Horizontal lines indicate FDR q < 0.05. Vertical lines show
log2 fold change greater than ±1, and can be read as non-standardized effect sizes. Signiﬁcant genes highlighted in red. B Manhattan plots for
ACC and Caudate. Horizontal red lines indicate FDR q < 0.05. Protein coding genes show their HGNC symbols, and lncRNA hits are marked by
their Ensemble Gene ID.
G. Sudre et al.
795
Molecular Psychiatry (2023) 28:792 – 800
ACC DEGs would enrich genes preferentially expressed in the ACC
in adolescence and adulthood. Consistent with this prediction, the
caudate DEGs were preferentially expressed in the prenatal and
infant caudate (Fig. 3 and Supplementary File 1). In contrast, the
ACC DEGs are expressed in primarily during adulthood, although
enrichment in infant life also hovered at signiﬁcance levels.
Normalized GSEA enrichment scores are given (Supplementary
File 1; GSEA developmental tabs) to provide an impression of how
ADHD-related change in the transcriptome aligns with genes
expressed
at
different
stages.
This
dissociation
is
broadly
consistent with concept that altered gene expression in the
caudate is more readily detected among genes preferentially
expressed in early life, whereas altered gene expression in the ACC
may also encompass genes expressed at later developmental
stages.
Common and rare genetic risk for ADHD and differential gene
expression
In line with expectations, by using MAGMA analyses we found
DEGs implicated in ADHD through GWAS overlapped signiﬁcantly
with DEGs in both the post-mortem ACC (p = 0.003), and caudate
(p = 0.02). Considering rare variant risk for ADHD, caudate DEGs
show a trend toward enrichment among genes that harbor CNVs
in ADHD (p = 0.06) but this relationship was not found for ACC
DEGs (p = 0 0.91).
Transdiagnostic transcriptomic signatures
We looked at correlations between DEGs in ADHD and other
psychiatric disorders (Fig. 4A). For the caudate, signiﬁcant correla-
tions were found between the ADHD transcriptome and autistic
spectrum disorder (median rho = 0.19; 95th centiles 0.121–0.252,
p < 0.0001),
bipolar
affective
disorder
(0.164
[0.079–0.377],
p = 0.008),
major
depression
(0.07
[0.053–0.084],
p < 0.0001),
obsessive compulsive disorder (0.305 [0.288–0.321], p < 0.0001),
and
schizophrenia
(0.189
[0.111–0.265],
p < 0.0001).
For
the
cingulate cortex, signiﬁcant correlations emerged between the
ADHD transcriptome and the transcriptome in autistic spectrum
disorder
(median
rho = 0.166;
95th
centiles
0.102–0.257,
p < 0.0001), and major depression (0.186 [0.066–0.397], p = 0.02),
but not for schizophrenia (0.216 [0.053–0.461], p = 0.056) or bipolar
affective disorder (0.197 [0.031–0.447], p = 0.22). This ﬁnding adds
ADHD to the list of disorders that show similarities in their neural
transcriptomic proﬁle.
The
DEGs
in
the
post-mortem
ADHD
brain
were
also
signiﬁcantly
related
to
SNP
risk
for
schizophrenia
(ACC:
p = 0.002; caudate: p = 5.2 × 10−9) and bipolar disorder (ACC:
−4
0
4
pan−developmental
prenatal
infant (0−2 yrs)
child (3−11 yrs)
adolescent (12−19 yrs)
adult (>19 yrs)
ACC
Caudate
log10 (p)
Fig. 3
GSEA results for region-speciﬁc developmental sets in ACC
and Caudate. Color scale indicates the absolute log10 of the nominal
p value, using the sign of the normalized enrichment score (blue
meaning upregulation in ADHD during that developmental period,
and red downregulation in ADHD). Results marked with thicker
borders are signiﬁcant after correction for multiple comparisons
(FDR, q < 0.05).
neurotransmitter receptor activity
tau protein binding
tau−protein kinase activity
dynein light chain binding
taste receptor activity
fatty acid derivative binding
ephrin receptor binding
glutamate receptor binding
glutamate receptor activity
0
1
2
3
4
 −log10 (padjusted)
Caudate
GABA receptor activity
serotonin receptor activity
structural constituent of muscle
neurotransmitter receptor activity
immunoglobulin binding
extracellular matrix structural constituent
0
1
2
3
4
 −log10 (padjusted)
ACC
A
GABA−ergic synapse
mitochondrial protein complex
transporter complex
axon part
Schaffer collateral − CA1 synapse
neuron to neuron synapse
postsynaptic specialization
glutamatergic synapse
synaptic membrane
neuron spine
0
1
2
3
4
5
 −log10 (padjusted)
Caudate
phagocytic cup
actin cytoskeleton
contractile fiber
microtubule organizing center part
cell−substrate junction
platelet alpha granule
PML body
extracellular matrix
collagen trimer
blood microparticle
0
1
2
3
4
5
 −log10 (padjusted)
ACC
B
Fig. 2
Gene set enrichments analyses results. A Molecular function gene ontology. All signiﬁcant sets (FDR q < 0.05) for each region are
displayed. B GSEA results for top 10 cellular components gene ontology. Gene sets pertaining to neural features and neurotransmitters are
indicated in red. Dotted line indicates FDR q < 0.05, dashed line FDR q < 0.1.
G. Sudre et al.
796
Molecular Psychiatry (2023) 28:792 – 800
p = 3.1 × 10−5; caudate: p = 2.8 × 10−5) (Fig. 4B). Notably, none of
the ADHD participants in this study had schizophrenia and only
one had bipolar affective disorder as a comorbidity. Genes
differentially expressed in the post-mortem ACC, but not the
caudate were nominally signiﬁcant when tested for association
with SNP risk for major depressive disorder (p = 0.04).
Analyses conﬁned to the largest subpopulation
We repeated analyses using the largest subpopulation (white,
non-Hispanic). A similar pattern of results emerged (Supplemen-
tary Table 5, Supplementary Figs. 9–12, and Supplementary File 2).
Speciﬁcally, two genes showed signiﬁcant differential expression
in the ACC at FDR q < 0.05 for both the entire cohort and white
non-Hispanic subpopulation (CCDC13 and HILPDA, and six genes
showed differential expression at FDR q < 0.1 for both cohorts
(MYO1G, ANGPTL4, CCL2, KIAA0040, JPH2, and ITPK). The single
signiﬁcant caudate DEG in the initial analysis did not hold for the
white, non-Hispanic cohort only. GSEA analyses also very similar
results when performed on the white, non-Hispanic cohort
compared to the entire cohort. Thus, for the white, non-Hispanic
cohort alone, DEG in the ACC signiﬁcantly enriched genes
expressed in the ACC in adult life, and DEG in caudate enriched
genes expressed in the infant caudate (Supplementary Fig. 9 and
Supplementary File 2). Similarly, DEG in the white, non-Hispanic
cohort
showed
enrichment
of
gene
sets
pertaining
to
neurotransmitter receptor activity, including serotonin and GABA
in the ACC, and glutamate in the caudate (Supplementary Fig. 10
and Supplementary File 2). Association between DEG in the
caudate and SNP risk for bipolar affective disorder (p = 0.0007)
and schizophrenia (p = 0.03) held, as did associations between
DEG in the ACC and SNP risk for bipolar affective disorder
(p = 0.001) and major depressive disorder (p = 0.04) (Supplemen-
tary Fig. 11). Finally, the correlations between transcriptome across
different neuropsychiatric disorders held for the white, non-
Hispanic group (Supplementary Fig. 12).
Results also held in analyses that did not covary for comorbid
disorders (Supplementary File 3). At the single gene level, nine
genes remained signiﬁcantly associated with ADHD (Supplemen-
tary Table 5). Additionally, DEG in the ACC signiﬁcantly enriched
genes expressed in the ACC in adult life, whereas DEG in caudate
enriched genes expressed in the infant caudate (Supplementary
Fig. 13). The pattern of enrichment of neurotransmitter gene sets
(Supplementary Fig. 14) also closely resembled that seen for the
main analysis. Correlations between transcriptome across different
neuropsychiatric disorders held, as did the pattern of associated
SNP risk (Supplementary Figs. 15 and 16). Findings were also
robust when those with comorbid MDD were removed (Supple-
mentary File 4, Supplementary Tables 5 and 7 and Supplementary
Figs. 17–20). A summary of all robustness analyses is given as
Supplementary Table 7.
0.0
0.2
0.4
0.6
ASD [2]
ASD [8]
ASD [7]
ASD [1]
SCZ [3]
SCZ [2]
SCZ [1]
BD [3]
BD [2]
BD [1]
MDD [3]
MDD [1]
ACC
0.0
0.2
0.4
0.6
ASD [2]
ASD [1]
SCZ [4]
SCZ [2]
SCZ [1]
BD [5]
BD [2]
BD [1]
MDD [1]
OCD [6]
Caudate
Disorders
Autism Spectrum Disorder
Schizophrenia
Bipolar Disorder
Major Depression Disorder
Obsessive Compulsive Disorder
Transcriptome correlation (rho)
A
0
8.5
ASD
OCD
BD
SCZ
TS
MDD
PTSD
AUD
ACC
Caudate
 −log10 (p)
B
Fig. 4
Transdiagnostic transcriptomic analyses results. A Correlation between differentially expressed genes in the ACC and Caudate in our
dataset and other disorders. Number indicates the data source: [1] Gandal et al. [65] (microarray), [2] Gandal et al. [65] (RNA-seq), [3] Akula et al.
[66], [4] Benjamin et al. [67], [5] Paciﬁco and Davis [68], [6] Piantadosi et al. [69], [7] Wright et al. [70], [8] Parikshak et al. [71]. B Enrichment of
DEGs in the ACC and caudate among genes implicated by GWAS of other disorders (analyses using MAGMA). The “X” indicates non-signiﬁcant
enrichment (p < 0.05). The circle size indicates the absolute log10 of the nominal p value. ASD autism spectrum disorder, OCD obsessive
compulsive disorder, BD bipolar disorder, SCZ schizophrenia, TS Tourette syndrome, MDD major depressive disorder, PTSD post-traumatic
stress disorder, AUD alcohol use disorders. ASD, TS, and AUD results use European population only for estimating linkage disequilibrium.
G. Sudre et al.
797
Molecular Psychiatry (2023) 28:792 – 800

## Clinical Significance
conclusion, this study of the ADHD post-mortem transcrip-
tome demonstrates alterations in cortico-striatal gene expression
that inform both developmental and neurotransmitter-based
models of the disorder.
DATA AVAILABILITY
Data are being deposited in NIMH Data Archive under Collection 3151, experiment
2056 (https://nda.nih.gov/edit_collection.html?id=3151), with the https://doi.org/
10.15154/1527972.
CODE AVAILABILITY
Code used for analyses and ﬁgures is deposited here: https://zenodo.org/badge/
latestdoi/505945767, with the https://doi.org/10.5281/zenodo.6798439.

## References
REFERENCES
1. Faraone SV, Larsson H. Genetics of attention deﬁcit hyperactivity disorder. Mol
Psychiatry. 2019;24:562–75.
2. Demontis D, Walters RK, Martin J, Mattheisen M, Als TD, Agerbo E, et al. Discovery
of the ﬁrst genome-wide signiﬁcant risk loci for attention deﬁcit/hyperactivity
disorder. Nat Genet. 2019;51:63–75.
3. Harich B, van der Voet M, Klein M, Čížek P, Fenckova M, Schenck A, et al. From
rare copy number variants to biological processes in ADHD. Am J Psychiatry.
2020;177:855–66.
4...
---
