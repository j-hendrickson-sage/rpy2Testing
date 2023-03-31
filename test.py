import rpy2

import rpy2.robjects.packages as rpackages

packnames = ('DESeq2',)
utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)
packnames_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
if len(packnames_to_install) > 0:
    utils.install_packages(StrVector(packnames_to_install))