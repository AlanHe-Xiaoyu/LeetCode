# Robot Simulator

- Maintainer: @shane.rogers

## Overview

Goal is write a relatively simple class which tests standard OOP skills,
communication and collaboration. The candidate is asked to write a Robot
simulator, which involves placing individual Robots on a hypothetical grid. Each
Robot can responds to certain commands and has internal state which relates to
its current coordinates on the grid and its bearing. The most simple
implementations involve a lot of control flow and duplication of logic, better
implementations are more terse.

## Overview

- Write a robot simulator, where robots can be placed on an infinite 2D grid,
  with cardinal directions of North, South, East and West.
- Robots will always be facing in one of the cardinal directions and also have
  co-ordinates on the grid (e.g. `{x: 3, y: 8}`)
- Movement in any direction on the grid is a change of 1 unit
- Robots can respond perform a variety of actions which update their
  co-ordinates and orientation on the board as described below

```
// Robot properties
bearing - direction the robot is facing
coordinates - x,y position on the grid

// Robot methods
orient('north') - sets the robot's bearing by the passed cardinal direction
turnRight() - updates the robot's bearing
turnLeft()  - updates the robot's bearing
at(1,2) - sets the robots co-ordinates by the argument count (i.e. 1)
advance(1) - updates the robot's co-ordinates (based on it's current bearing) by the argument count (i.e. 1)
instructions('ALA') - converts an encoded instructions string to a list of methods
place({x: 2, y: -7, direction: 'east'}) - sets both the robot's co-ordinates and bearing
evaluate('ALA') - will execute the passed instructions on the robot

// Expectations
expect(robot.instructions('RAAL')).toEqual(['turnRight', 'advance', 'advance', 'turnLeft']);
robot.place({x: 2, y: -7, direction: 'east'});
robot.evaluate('RRAAAAALA');
expect(robot.coordinates).toEqual([-3, -8]);
expect(robot.bearing).toEqual('south');
```

- Implement a Robot simulator which can satisfy all of the expectations listed
  above

---

## Rubric (Coding)

#### Unfamiliar

Negative signs:

- Can't get close to a working solution
- Doesn't break the problem into incremental steps
- Doesn't have a debugging methodology
- Is non-communicative

#### Familiar

Positive signs:

- Gets to a working solution
- Is communicative and asks qualifying questions
- Progressively validates their solution

Negative signs:

- Code is hard to read and poorly factored

#### Proficient

Positive signs:

- Proactively refactors to a simpler more readable solution
- Adds documentation to the code

Negative signs:

- Uses lots of repetitive if else statements and cant refactor to more robust
  solution

#### Master

Positive signs:

- Proactively handles error cases with useful output
- Can refactor turn command to handle all intercardinal directions like NE, SW
  etc and talk through how advancing in those directions might be handled.

---

## Example Solutions

- [Language](#Language)

# Language

```javascript
const BEARINGS = ["north", "east", "south", "west"]
const INSTRUCTION_MAP = {
  L: "turnLeft",
  R: "turnRight",
  A: "advance"
}

export default class Robot {
  constructor() {
    this.bearing = "north"
    this.coordinates = [0, 0]
  }

  orient(bearing) {
    this.bearing = bearing
  }

  turnRight() {
    this.turn(1)
  }

  turnLeft() {
    this.turn(-1)
  }

  turn(step) {
    const newIndex = (BEARINGS.indexOf(this.bearing) + step) % BEARINGS.length
    const newBearing = BEARINGS.slice(newIndex)[0]

    if (newBearing) {
      this.bearing = newBearing
    } else {
      throw new Error("Index out of bounds")
    }
  }

  at(x, y) {
    this.coordinates = [x, y]
  }

  advance(step = 1) {
    const advanceMap = {
      east: [step, 0],
      west: [-step, 0],
      north: [0, step],
      south: [0, -step]
    }
    const coords = advanceMap[this.bearing]

    this.coordinates[0] += coords[0]
    this.coordinates[1] += coords[1]
  }

  instructions(command) {
    return command.split("").map(char => INSTRUCTION_MAP[char])
  }

  place({ x, y, direction }) {
    this.bearing = direction
    this.coordinates = [x, y]
  }

  evaluate(command) {
    const instructions = this.instructions(command)
    instructions.forEach(instruction => this[instruction]())
  }
}
```
