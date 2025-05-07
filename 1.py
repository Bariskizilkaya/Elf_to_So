import lief
import sys
path = sys.argv[1]
bin_ = lief.parse(path)
bin_[lief.ELF.DynamicEntry.TAG.FLAGS_1].remove(lief.ELF.DynamicEntryFlags.FLAG.PIE)
bin_.write(path + ".patched")