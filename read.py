+try:
+    with open("names.csv") as file:
+        for line in file:
+            line = line.rstrip()
+            if ',' not in line:
+                continue  # Skip malformed lines
+            parts = line.split(",")
+            if len(parts) != 2:
+                continue  # Skip lines without exactly 2 values
+            name, age = parts
+            print(f"{name}'s age is {age}")
+except FileNotFoundError:
+    print("Error: names.csv not found")
