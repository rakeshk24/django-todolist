+try:
+    file = open("names.csv")
+    data = file.readlines()
+    for line in data:
+        line = line.strip()
+        if len(line) == 0:
+            continue
+        if ',' not in line:
+            print("bad line:", line)
+            continue
+        parts = line.split(",")
+        if len(parts) < 2:
+            continue
+        name = parts[0]
+        if len(parts) > 1:
+            age = parts[1]
+        else:
+            age = "unknown"
+        print(name + " is " + age + " years old")
+    file.close()
+except:
+    print("Something went wrong :(")
