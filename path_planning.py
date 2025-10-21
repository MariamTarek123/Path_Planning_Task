from __future__ import annotations

from typing import List

from PIL.ImageChops import offset

from src.models import CarPose, Cone, Path2D


class PathPlanning:
    """Student-implemented path planner.

    You are given the car pose and an array of detected cones, each cone with (x, y, color)
    where color is 0 for yellow (right side) and 1 for blue (left side). The goal is to
    generate a sequence of path points that the car should follow.

    Implement ONLY the generatePath function.
    """

    def __init__(self, car_pose: CarPose, cones: List[Cone]):
        self.car_pose = car_pose
        self.cones = cones

    def generatePath(self) -> Path2D:
        """Return a list of path points (x, y) in world frame.

        Requirements and notes:
        - Cones: color==0 (yellow) are on the RIGHT of the track; color==1 (blue) are on the LEFT.
        - You may be given 2, 1, or 0 cones on each side.
        - Use the car pose (x, y, yaw) to seed your path direction if needed.
        - Return a drivable path that stays between left (blue) and right (yellow) cones.
        - The returned path will be visualized by PathTester.

        The path can contain as many points as you like, but it should be between 5-10 meters,
        with a step size <= 0.5. Units are meters.

        Replace the placeholder implementation below with your algorithm.
        """

        """  color ==1 (blue)
             color ==0 (yellow)
             if both cones exist the car should go in the middle (midpoint)
             if no cones exist (0) the car will drive straight
             if 1 cone exists (1) the car will drive a bit offset from that side
         """
        import math
        #separate cones  - attributes: (x,y) and color
        blue = []
        yellow = []
        for c in self.cones:
            if c.color == 1:  #blue cone, left side
                blue.append((c.x, c.y))
            elif c.color == 0:  #yellow cone, right side
                yellow.append((c.x, c.y))

        car = self.car_pose  #car position and yaw
        car_x, car_y = 0.0,0.0 # to start from position (0,0)
        car_yaw=car.yaw
        path = []

        steps=0.5
        total=10
        num_steps = int(total / steps)

        def avg(points): # find the avg position
            if len(points) == 0:
                return None
            elif len(points) == 1:
                return points[0]
            elif len(points) == 2:
                return (points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2
           # part 2: if given up to 3 cones
            elif len(points) == 3:
                return (points[0][0] + points[1][0] + points[2][0]) / 3, (points[0][1] + points[1][1] + points[2][1]) / 3

        blue_avg = avg(blue)
        yellow_avg = avg(yellow)

        #Case 1: both cones exist
        if blue_avg and yellow_avg:
            center_x = (blue_avg[0] + yellow_avg[0]) / 2
            center_y = (blue_avg[1] + yellow_avg[1]) / 2

        #Case 2: only blue exist - moves a little away from that cone
        elif blue_avg and not yellow_avg:
            offset = 1.0
            right_x = math.sin(car_yaw)
            right_y = -math.cos(car_yaw)
            center_x = blue_avg[0] + right_x * offset
            center_y = blue_avg[1] + right_y * offset

        #Case 3: only Yellow exist
        elif yellow_avg and not blue_avg:
            offset = 1.0
            left_x = -math.sin(car_yaw)
            left_y = math.cos(car_yaw)
            center_x = yellow_avg[0] + left_x * offset
            center_y = yellow_avg[1] + left_y * offset

        #Case 4: No cones
        else:
            center_x = car_x + math.cos(car_yaw) * 5
            center_y = car_y + math.sin(car_yaw) * 5

        # Compute new heading direction toward the target (center_x, center_y)
        dx = center_x - car_x
        dy = center_y - car_y
        new_yaw = math.atan2(dy, dx)

        #  Go straight for 2 meters 
        straight_distance = 2.0
        steps = 0.5
        straight_steps = int(straight_distance / steps)
        path = []
    
        
    

        # Generate path
        for i in range(num_steps):
            px = car_x + math.cos(new_yaw) * i * steps
            py = car_y + math.sin(new_yaw) * i * steps
            path.append((px, py))

        return path
