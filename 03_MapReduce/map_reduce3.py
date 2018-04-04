--- map_reduce.py	(original)
+++ map_reduce.py	(refactored)
@@ -25,12 +25,13 @@
 
 import sys
 import re
+from functools import reduce
 try:
     import simplejson as json
 except ImportError:
     import json
 
-import __builtin__
+import builtins
 
 def map(line):
     pass
@@ -45,7 +46,7 @@
     Emits a key->value pair.  Key and value should be strings.
     """
     try:
-        print "\t".join( (key, value) )
+        print("\t".join( (key, value) ))
     except:
         pass
 
@@ -53,7 +54,7 @@
     """Calls map() for each input value."""
     for line in sys.stdin:
         line = line.rstrip()
-        map(line)
+        list(map(line))
 
 def run_reduce():
     """Gathers reduce() data in memory, and calls reduce()."""
@@ -76,7 +77,7 @@
 def main():
     """Runs map or reduce code, per arguments."""
     if len(sys.argv) != 2 or sys.argv[1] not in ("map", "reduce"):
-        print "Usage: %s <map|reduce>" % sys.argv[0]
+        print("Usage: %s <map|reduce>" % sys.argv[0])
         sys.exit(1)
     if sys.argv[1] == "map":
         run_map()
