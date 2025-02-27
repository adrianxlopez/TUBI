# TUBI Tumor Map project

#### Goal
Software that could apply a clustering algorithm to the Treehouse TumorMap data.  It would be useful to be able to tune the algorithm by changing the number of clusters or other features.
Data
XY coordinate (or hexagonal coordinate) data from TumorMap ~1 MB. (Go to TumorMap, select Treehouse/TumorCompendium_v11_polyA; from the menu choose File|Download|XY coordinates)
TumorMap clinical data ~5 MB. (Can be downloaded from here.)

- Note: TumorCompendium_v11_polyA is our largest compendium. If you want to start with a smaller compendium, I recommend the Tumor Compendium v9 Public Ribodeplete (March 2019). All compendia are listed at https://treehousegenomics.soe.ucsc.edu/public-data.

#### Steps
1. Cluster Assignments for TumorMap Samples
   
> Apply a machine learning algorithm to the XY (or hex) coordinate data to define cluster assignments.  Review cluster assignments with Treehouse research team after uploading data to TumorMap as a feature.

2.  Refining the Clustering Algorithm
   
> After having a working prototype, manual review of the cluster assignments can take place to better fine tune the algorithm.
Tune hyperparameters (ex. number of clusters, stringency)
Use different clustering algorithms.  Can determine whether other algorithms provide clustering assignments that appear to fit the data better and are easier to run (ex. faster, require less resources, more easy to run by researcher).

3. Validate Algorithm on Multiple TumorMaps
> It would be great to be able to use this algorithm on TumorMaps consisting of different sample data.  Treehouse works with PolyA, ribo-deplete, cell line, xenograft and normal tissue data.  A useful algorithm would also be able to be used when slight perturbations occur in the sample data (ex. removing or adding small numbers of samples, removing or adding small numbers of genes).  This will help Treehouse in evaluating how different methods of processing data affect TumorMap visualizations.

