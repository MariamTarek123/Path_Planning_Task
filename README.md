### **1️ Cone Classification**
- Cones are divided into two lists to identify the sides of the track:  
  - **Blue cones (color == 1)** :left side  
  - **Yellow cones (color == 0)** : right side  

---

### **2 Average Function (avg(points))**
Calculates the average position of cones on each side to find the center of the track:
- 0 cones → returns None
- 1 cone → returns its position
- 2 cones → returns the midpoint
- 3 cones (added for part 2 of the task) → returns the average position of the three

 This lets the algorithm handle up to **3 cones per side** smoothly.

---

### **3 Handling Different Cases**
| Case | Description | Behavior |
|------|--------------|-----------|
| 1 | If Both sides have cones | The car moves through the midpoint between yellow and blue cones |
| 2 | If Only one side has cones | The car offsets  1 meter away from that cone either left or right depending on the cone's color |
| 3 | If No cones detected | The car drives straight ahead |

---

### **4 Path Generation**
Once the target direction is known which is the center of both x and y components
- The angle is computed   
- The car moves forward in steps (0.5 m)

---

###  Note:
The current algorithm implemented only moves in straight line toward the computed center, still configuring the turning and curve handling part so a few test cases failed, but will be configured soon inshallah :)


