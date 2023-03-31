#sudo apt-get install -y libharfbuzz-dev  libfribidi-dev libtiff-dev

install.packages("tidyverse")

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("DESeq2")