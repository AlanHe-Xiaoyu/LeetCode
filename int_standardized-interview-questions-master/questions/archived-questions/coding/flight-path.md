# Flight Path
- Maintainer: @yotam.mosinzon

## Overview

This question asks the candidate to implement an algorithm determining a flight path. It outlines a basic problem with several options to add complxity. The core technical areas tested are basic data structures and algorithms, but it allows opportunity to explore how a candidate approaches problem generalization and handling a broader set of concerns.

## Prompts

This problem is presented as a single prompt, given in a format that might appear in a work ticket:

```
// Given a list of flights (in any order), construct the trip
// that this list represents. For example, if we have a flight
// from San Francisco to Dallas and a flight from Los Angeles
// to San Francisco, the trip is "LAX to SFO to DFW".
//
// Assumptions:
// - Each city will be visited only once.
// - The list will only represent one single trip.
//
// flights = [('SFO', 'DFW'), ('LAX', 'SFO'), ('DFW', 'CLT')]
//
// Trip: ['LAX', 'SFO', 'DFW', 'CLT']
//
// If the above works, try your program with the following input:
// flights = [('DFW', 'CLT'), ('SFO', 'DFW'), ('WAS', 'NYK'), ('LAX', 'SFO'), ('CLT', 'WAS')]
// Trip: ['LAX', 'SFO', 'DFW', 'CLT', 'WAS', 'NYK']
```

This is normally copy/pasted directly into an editor, and the candidate should be asked to read through the question and encouraged to ask any questions they might have.

----

#### Expected questions from the candidate

- Input Types: a list of pairs of strings.
    C++ => vector<pair<string, string> >
    Java => ArrayList<Pair<String, String>>
    Python => [()]

- Running Time: try to get a working solution, then optimize.

#### What do we want to see/hear?

- The data structure is a critical component for this problem to not go O(n^2). Good candidates will break the problem into parts, first finding the start or end and going from there. This problem can be solved in O(n^2) (brute force), which is a non-ideal solution. There are some data structures and algorithms that result in O(n log n) but an ideal solution of O(n) can be achieved using the Set data structure (there are probably other ways) for finding the first airport and a map to find the flight path.

## Example Solutions

- [C#](#c)
- [Scala](#scala)
- [Java](#java)

# C#

```C#
using System;
using System.Linq;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        var flights = new List<Flight>
        {
            new Flight() { Origin = "ORD", Destination = "DNV" },
            new Flight() { Origin = "SFO", Destination = "NYC" },
            new Flight() { Origin = "LAX", Destination = "SFO" },
            new Flight() { Origin = "NYC", Destination = "ORD" },
        };

        //This algorithm assumes the list of flights contains no loops (who flies that way?).
        var flightMap = flights.ToDictionary(x => x.Origin, x => x.Destination);
        var origins = flights.Select(x => x.Origin).ToHashSet();
        var destinations = flights.Select(x => x.Destination).ToHashSet();

        var tripOrigin = origins.Except(destinations).Single();

        var trip = new List<String> { tripOrigin };

        var curOrigin = tripOrigin;
        while(flightMap.ContainsKey(curOrigin)) //We're done when we've got no where left to go
        {
            //Add the destination to the trip
            trip.Add(flightMap[curOrigin]);

            //The destination is the new origin for the next flight
            curOrigin = flightMap[curOrigin];
        }

        Console.WriteLine(String.Join(" -> ", trip));
    }
}

class Flight
{
    public String Origin { get; set; }
    public String Destination { get; set; }
}
```

# Scala

```Scala
object Solution extends App {
  val flightPath = findFlightPath(Seq(("DFW", "CLT"), ("SFO", "DFW"), ("WAS", "NYK"), ("LAX", "SFO"), ("CLT", "WAS")))
  println(flightPath)

  def findFlightPath(flights: Seq[(String, String)]): Seq[String] = {
    val secondSet: Set[String] = flights.map(_._2).toSet
    val first: String = flights.flatMap(x => Seq(x._1, x._2)).filterNot(secondSet.contains).head
    val flightMap: Map[String, String] = flights.toMap

    def recFlightMap(first: String, flightMap: Map[String, String]): Seq[String] =
      if (flightMap.contains(first))
        Seq(first) ++ recFlightMap(flightMap(first), flightMap - first)
      else
        Seq(first)

    recFlightMap(first, flightMap)
  }
}
```

# Java

```Java
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;

class Solution {

    static Map<String,String> flights = Map.of(
            "DFW", "CLT",
            "SFO", "DFW",
            "WAS", "NYK",
            "LAX", "SFO",
            "CLT", "WAS");

    public static void main(String[] args) throws Exception {

        // Not going to handle multiple departures from the same origin well.
        String origin = flights.keySet().stream().dropWhile(flights.values()::contains)
                .findFirst().orElseThrow(() -> new Exception("Why are you flying in circles?"));

        // Let's go flying! When we reach a destination that has no matching departure, we've arrived.
        Set<String> trip = new LinkedHashSet<>(Collections.singletonList(origin));
        for (String departing = origin; flights.containsKey(departing); ) {
            String destination = flights.get(departing);
            trip.add(destination);
            departing = destination;
        }

        System.out.println(String.join(" -> ", trip));

    }

}
```
