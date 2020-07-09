# Loan Sorting

## Overview

A loan has the following data points:

- Lender (string)
- Preapproved (boolean)
- APR (float)

You’re given a list of loans, a desired page size, and need to paginate them
with certain constraints:

- Each page has at most `pageSize` items.
- A preapproved loan must be the first item on each page if one is available.
  Preapproved loans cannot show up in any other position other than first. Make
  new pages if necessary.
- A lender appears at most once on each page. Make new pages if necessary.
- Without violating the above constraints, return loans sorted in increasing APR
  since lower is better.
- Without violating the above constraints, pages should be maximally compact
  (return the fewest possible pages).

## Rubric

This is an exercise in implementing real product requirements. There’s no need
for fancy DP, recursion, or other algorithms that are rarely relevant to real
engineering.

## Rubric (Coding)

Performance should not be a concern unless egregiously bad. In real engineering,
code complexity and readability matter way more than performance.

#### Characteristics of Unfamiliar

- Can't get to a working solution
- Often have piles and piles of if statements
- Are written in imperative style (especially bad if they choose Scala)
- Are poorly factored or hard to read

#### Characteristics of Familiar

- Gets to a working solution for a single test case
- Often have piles and piles of if statements
- Are written in imperative style (especially bad if they choose Scala)
- Are poorly factored or hard to read
- Algorithm is needlessly complex

#### Characteristics of Proficient

- Gets to a working solution for different test cases (e.g., changing the page size)
- Uses functional paradigms
- Algorithm is clean

#### Characteristics of Master

- Gets to a working solution for different test cases (e.g., changing the page size)
- Uses functional paradigms
- Algorithm is minimally complex and could be used as an example solution

## Starter Code

### Java

```java
import java.io.*;
import java.util.*;

class Loan {
  double apr;
  String lender;
  boolean preApproved;

  public Loan(double apr, String lender, boolean preApproved) {
    this.apr = apr;
    this.lender = lender;
    this.preApproved = preApproved;
  }

  public double getApr() {
    return this.apr;
  }

  public String getLender() {
    return this.lender;
  }

  public boolean getPreApproved() {
    return this.preApproved;
  }

  @Override
  public String toString() {
    return "Loan(" + this.apr + ", " + this.lender + ", " + this.preApproved + ")";
  }
}

class Solution {
  private static List<Loan> loans = Arrays.asList(
    new Loan(0.23, "Wells Fargo", false),
    new Loan(0.24, "Wells Fargo", true),
    new Loan(0.21, "Upstart", false),
    new Loan(0.19, "LendingTree", false),
    new Loan(0.20, "Upstart", true),
    new Loan(0.25, "Wells Fargo", true),
    new Loan(0.28, "Bank of America", true),
    new Loan(0.29, "Wells Fargo", false),
    new Loan(0.31, "Wells Fargo", false)
  );

  private static List<List<Loan>> correctPagingFor3LoansPerPage = Arrays.asList(
    Arrays.asList(
      new Loan(0.20, "Upstart", true),
      new Loan(0.19, "LendingTree", false),
      new Loan(0.23, "Wells Fargo", false)
    ),
    Arrays.asList(
      new Loan(0.24, "Wells Fargo", true),
      new Loan(0.21, "Upstart", false)
    ),
    Arrays.asList(
      new Loan(0.25, "Wells Fargo", true)
    ),
    Arrays.asList(
      new Loan(0.28, "Bank of America", true),
      new Loan(0.29, "Wells Fargo", false)
    ),
    Arrays.asList(
      new Loan(0.31, "Wells Fargo", false)
    )
  );

  // Returns a list of pages of loans, subject to the following constraints:
  // * Each page has at most `pageSize` items.
  // * A preapproved loan must be the first item on each page if one
  //   is available. Preapproved loans cannot show up in any other position other than first. Make new pages if necessary.
  // * A lender appears at most once on each page. Make new pages if necessary.
  // * Without violating the above constraints, return loans sorted in increasing APR since lower is better.
  public static List<List<Loan>> getPages(List<Loan> loans, int pageSize) {
    List<List<Loan>> pages = new ArrayList<List<Loan>>();
    return pages;
  }

  public static void main(String[] args) {
    for (List<Loan> page : getPages(loans, 3)) {
      for (Loan loan : page) {
        System.out.println(loan.toString());
      }
      System.out.println("");
    }
  }
}
```

### Scala

```scala
object Solution extends App {
  case class Loan(apr: Double, lender: String, preApproved: Boolean)

  val loans = List(
    Loan(0.23, "Wells Fargo", false),
    Loan(0.24, "Wells Fargo", true),
    Loan(0.21, "Upstart", false),
    Loan(0.19, "LendingTree", false),
    Loan(0.20, "Upstart", true),
    Loan(0.25, "Wells Fargo", true),
    Loan(0.28, "Bank of America", true),
    Loan(0.29, "Wells Fargo", false),
    Loan(0.31, "Wells Fargo", false)
  )

  val correctPagingFor3LoansPerPage = List(
    List(
      new Loan(0.20, "Upstart", true),
      new Loan(0.19, "LendingTree", false),
      new Loan(0.23, "Wells Fargo", false)
    ),
    List(
      new Loan(0.24, "Wells Fargo", true),
      new Loan(0.21, "Upstart", false)
    ),
    List(
      new Loan(0.25, "Wells Fargo", true)
    ),
    List(
      new Loan(0.28, "Bank of America", true),
      new Loan(0.29, "Wells Fargo", false)
    ),
    List(
      new Loan(0.31, "Wells Fargo", false)
    )
  )

  // Returns a list of pages of loans, subject to the following constraints:
  // * Each page has at most `pageSize` items.
  // * A preapproved loan must be the first item on each page if one
  //   is available. Preapproved loans cannot show up in any other position other than first. Make new pages if necessary.
  // * A lender appears at most once on each page. Make new pages if necessary.
  // * Without violating the above constraints, return loans sorted in increasing APR since lower is better.
  // * Without violating the above constraints, pages should be maximally compact (return the fewest possible pages).
  def getPages(loans: List[Loan], pageSize: Int): List[List[Loan]] = {
    List(List[Loan]())
  }

  getPages(loans, 3).foreach { page =>
    page.foreach { loan =>
      println(loan)
    }
    println("")
  }
}
```

### Javascript

```javascript
function toString(loan) {
  return `Loan(${loan.apr}, ${loan.lender}, ${loan.preapproved})`
}

function loan(apr, lender, preapproved) {
  return {
    apr,
    lender,
    preapproved
  }
}

const loans = [
  loan(0.23, "Wells Fargo", false),
  loan(0.24, "Wells Fargo", true),
  loan(0.21, "Upstart", false),
  loan(0.19, "LendingTree", false),
  loan(0.2, "Upstart", true),
  loan(0.25, "Wells Fargo", true),
  loan(0.28, "Bank of America", true),
  loan(0.29, "Wells Fargo", false),
  loan(0.31, "Wells Fargo", false)
]

function correctPagingFor3LoansPerPage() {
  return [
    [
      loan(0.2, "Upstart", true),
      loan(0.19, "LendingTree", false),
      loan(0.23, "Wells Fargo", false)
    ],
    [loan(0.24, "Wells Fargo", true), loan(0.21, "Upstart", false)],
    [loan(0.25, "Wells Fargo", true)],
    [loan(0.28, "Bank of America", true), loan(0.29, "Wells Fargo", false)],
    [loan(0.31, "Wells Fargo", false)]
  ]
}

/*
  Returns a list of pages of loans, subject to the following constraints:
  * Each page has at most `pageSize` items.
  * A preapproved loan must be the first item on each page if one
    is available. Preapproved loans cannot show up in any other position other than first. Make new pages if necessary.
  * A lender appears at most once on each page. Make new pages if necessary.
  * Without violating the above constraints, return loans sorted in increasing APR since lower is better.
*/
function getPages(loans, pageSize) {
  return []
}

getPages(loans, 3).forEach(page => {
  page.forEach(l => console.log(toString(l)))
  console.log("")
})
console.log("")
```

<!-- prettier-ignore -->
### C#

```csharp
using System;
using System.Collections.Generic;

class Loan
{
  public double apr { get; private set; }
  public String lender { get; private set; }
  public bool preApproved { get; private set; }

  public Loan(double apr, String lender, bool preApproved)
  {
    this.apr = apr;
    this.lender = lender;
    this.preApproved = preApproved;
  }

  public override String ToString()
  {
    return "Loan(" + this.apr + ", " + this.lender + ", " + this.preApproved + ")";
  }
}

class Solution
{
  private static List<Loan> loans = new List<Loan>
  {
    new Loan(0.23, "Wells Fargo", false),
    new Loan(0.24, "Wells Fargo", true),
    new Loan(0.21, "Upstart", false),
    new Loan(0.19, "LendingTree", false),
    new Loan(0.20, "Upstart", true),
    new Loan(0.25, "Wells Fargo", true),
    new Loan(0.28, "Bank of America", true),
    new Loan(0.29, "Wells Fargo", false),
    new Loan(0.31, "Wells Fargo", false)
  };

  private static List<List<Loan>> correctPagingFor3LoansPerPage = new List<List<Loan>>
  {
    new List<Loan>
    {
      new Loan(0.20, "Upstart", true),
      new Loan(0.19, "LendingTree", false),
      new Loan(0.23, "Wells Fargo", false)
    },
    new List<Loan>
    {
      new Loan(0.24, "Wells Fargo", true),
      new Loan(0.21, "Upstart", false)
    },
    new List<Loan>
    {
      new Loan(0.25, "Wells Fargo", true)
    },
    new List<Loan>
    {
      new Loan(0.28, "Bank of America", true),
      new Loan(0.29, "Wells Fargo", false)
    },
    new List<Loan>
    {
      new Loan(0.31, "Wells Fargo", false)
    }
  };

  // Returns a list of pages of loans, subject to the following constraints:
  // * Each page has at most `pageSize` items.
  // * A preapproved loan must be the first item on each page if one
  //   is available. Preapproved loans cannot show up in any other position other than first. Make new pages if necessary.
  // * A lender appears at most once on each page. Make new pages if necessary.
  // * Without violating the above constraints, return loans sorted in increasing APR since lower is better.
  public static List<List<Loan>> getPages(List<Loan> loans, int pageSize)
  {
    var pages = new List<List<Loan>>();
    return pages;
  }

  public static void Main(String[] args)
  {
    foreach (var page in getPages(loans, 3))
    {
      foreach (var loan in page)
      {
        Console.WriteLine(loan);
      }

      Console.WriteLine("");
    }
  }
}
```

### Python

```python
from collections import namedtuple

Loan = namedtuple('Loan', 'apr lender preapproved')

LOANS = [
  Loan(0.23, "Wells Fargo", False),
  Loan(0.24, "Wells Fargo", True),
  Loan(0.21, "Upstart", False),
  Loan(0.19, "LendingTree", False),
  Loan(0.20, "Upstart", True),
  Loan(0.25, "Wells Fargo", True),
  Loan(0.28, "Bank of America", True),
  Loan(0.29, "Wells Fargo", False),
  Loan(0.31, "Wells Fargo", false)
]

correctPagingFor3LoansPerPage = [
  [
    Loan(0.20, "Upstart", True),
    Loan(0.19, "LendingTree", False),
    Loan(0.23, "Wells Fargo", False)
  ],
  [
    Loan(0.24, "Wells Fargo", True),
    Loan(0.21, "Upstart", False)
  ],
  [
    Loan(0.25, "Wells Fargo", True)
  ],
  [
    Loan(0.28, "Bank of America", True),
    Loan(0.29, "Wells Fargo", False)
  ],
  [
    Loan(0.31, "Wells Fargo", False)
  ]
]

#  Returns a list of pages of loans, subject to the following constraints:
#  * Each page has at most `pageSize` items.
#  * A preapproved loan must be the first item on each page if one
#    is available. Preapproved loans cannot show up in any other position other than first. Make new pages if necessary.
#  * A lender appears at most once on each page. Make new pages if necessary.
#  * Without violating the above constraints, return loans sorted in increasing APR since lower is better.
def get_pages(loans, page_size):
  pass

for page in get_pages(LOANS, 3):
  for loan in page:
    print(loan)
  print('')
```

### PHP

```
$loans = array(
    new Loan(0.23, "Wells Fargo", false),
    new Loan(0.24, "Wells Fargo", true),
    new Loan(0.21, "Upstart", false),
    new Loan(0.19, "LendingTree", false),
    new Loan(0.20, "Upstart", true),
    new Loan(0.25, "Wells Fargo", true),
    new Loan(0.28, "Bank of America", true),
    new Loan(0.29, "Wells Fargo", false),
    new Loan(0.31, "Wells Fargo", false)
);

$correctPagingFor3LoansPerPage = [
    [
        new Loan(0.20, "Upstart", true),
        new Loan(0.19, "LendingTree", false),
        new Loan(0.23, "Wells Fargo", false)
    ],
    [
        new Loan(0.24, "Wells Fargo", true),
        new Loan(0.21, "Upstart", false)
    ],
    [
        new Loan(0.25, "Wells Fargo", true)
    ],
    [
        new Loan(0.28, "Bank of America", true),
        new Loan(0.29, "Wells Fargo", false)
    ],
    [
        new Loan(0.31, "Wells Fargo", false)
    ]
];

function printPages($pages) {
    $pageNumber = 1;
    foreach($pages as $page) {
        echo "Page " . $pageNumber++ . "\n---------------------------------------------\n";
        foreach ($page as $loan) {
            echo $loan;
        }
        echo "\n";
    }
}

class Loan {
    public $lender;
    public $apr;
    public $preApproved;

    public function __construct($apr, $lender, $preApproved) {
        $this->lender = $lender;
        $this->apr = $apr;
        $this->preApproved = $preApproved;
    }

    public function __toString()
    {
        return $this->lender . " " . $this->apr . " " .
            ($this->preApproved ? "Pre-Approved" : "") . "\n";
    }
}
```

## Example Solutions

### Scala

```scala
def getPages(loans: List[Loan], pageSize: Int): List[List[Loan]] = {
  val (preapprovedLoans, normalLoans) = loans.sortBy(_.apr).partition(_.preApproved)

  normalLoans.foldLeft(preapprovedLoans.map(List(_))) { (currentPages, newLoan) =>
    val chosenPageIndex = currentPages
      .indexWhere(p => p.length < pageSize && !p.map(_.lender).contains(newLoan.lender))

    if (chosenPageIndex == -1) {
      currentPages ++ List(List(newLoan))
    } else {
      val page = currentPages(chosenPageIndex)
      currentPages.take(chosenPageIndex) ++ List(page ++ List(newLoan)) ++ currentPages.drop(chosenPageIndex + 1)
    }
  }
}
```

### Ruby

```ruby
Loan = Struct.new("Loan", :apr, :lender, :preapproved)

LOANS = [
  Loan.new(0.23, "Wells Fargo", false),
  Loan.new(0.24, "Wells Fargo", true),
  Loan.new(0.21, "Upstart", false),
  Loan.new(0.19, "LendingTree", false),
  Loan.new(0.20, "Upstart", true),
  Loan.new(0.25, "Wells Fargo", true),
  Loan.new(0.28, "Bank of America", true),
  Loan.new(0.24, "Wells Fargo", false),
]

def get_loans(loans, page_size)
  raise ArgumentError unless page_size >= 1
  sorted_loans = loans.sort_by(&:apr)

  pages = []

  while !sorted_loans.empty?
    page = []

    preapproved_offers, nonpreapproved_offers = sorted_loans.partition(&:preapproved)

    if !preapproved_offers.empty?
      page << preapproved_offers.first
      sorted_loans.delete(preapproved_offers.first)
    end

    while page.length < page_size && !sorted_loans.empty?
      used_lenders = page.map(&:lender)
      available_loan = nonpreapproved_offers.find { |l| !used_lenders.include?(l.lender) }
      break if available_loan.nil?

      page << available_loan
      sorted_loans.delete(available_loan)
    end

    pages << page
  end

  pages
end

puts get_loans(LOANS, 3).map { |page| page.map(&:inspect).join("\n") }.join("\n\n")
```

<!-- prettier-ignore -->
### C#

```csharp
public static List<List<Loan>> getPages(List<Loan> loans, int pageSize)
{
  var pages = new List<List<Loan>>();

  //order by apr (ascending) and separate loans by pre-approval status
  var partitionedLoans = loans.OrderBy(x => x.apr).ToLookup(x => x.preApproved);
  var (preApprovedLoans, otherLoans) = (partitionedLoans[true], partitionedLoans[false]);

  //Continue until we run out of loans to display
  while(preApprovedLoans.Any() || otherLoans.Any())
  {
    var currentPage = new List<Loan>(pageSize);

    //Get the preapproved loan for this page, if we have any left
    if(preApprovedLoans.Any())
    {
      var preApprovedLoanForPage = preApprovedLoans.First();
      preApprovedLoans = preApprovedLoans.Skip(1);
      currentPage.Add(preApprovedLoanForPage);
    }

    //Get the non-preapproved loans for this page
    var usedOtherLoans = new List<Loan>();
    foreach(var otherLoan in otherLoans)
    {
      //Only use the current loan if we don't already have a loan on the page for the lender
      if(!currentPage.Any(x => x.lender == otherLoan.lender))
      {
        currentPage.Add(otherLoan);

        //Since we can't modify the list while we're enumerating it, keep track of what
        //we've added to remove them later
        usedOtherLoans.Add(otherLoan);

        //If our page is full, we can stop looking for loans to add
        if(currentPage.Count() == pageSize) break;
      }
    }

    //Make sure we remove the loans we used from the pool
    otherLoans = otherLoans.Except(usedOtherLoans);

    pages.Add(currentPage);
  }

  return pages;
}
```

### Java

```java
    public static List<List<Loan>> getPages(List<Loan> loans, int pageSize) {
        List<Loan> sorted = new ArrayList<>(loans.size());
        sorted.addAll(loans);
        sorted.sort(Comparator.comparingDouble(Loan::getApr));

        Map<Boolean, List<Loan>> loansByPreapprovalStatus = sorted.stream().collect(Collectors.partitioningBy(Loan::getPreApproved));


        List<Loan> preApproved = loansByPreapprovalStatus.getOrDefault(true, Collections.emptyList());
        List<Loan> notPreApproved = loansByPreapprovalStatus.getOrDefault(false, Collections.emptyList());

        List<List<Loan>> pages = new ArrayList<>();

        while (!preApproved.isEmpty() && !notPreApproved.isEmpty()) {
            List<Loan> page = new ArrayList<>();
            Set<String> lenders = new HashSet<>();

            if (!preApproved.isEmpty()) {
                Loan nextPreapproved = preApproved.remove(0);
                page.add(nextPreapproved);
                lenders.add(nextPreapproved.getLender());
            }

            boolean keepSearching = true;
            while (page.size() < pageSize && keepSearching) {
                Optional<Loan> maybeLoan = notPreApproved.stream().filter((Loan l) -> !lenders.contains(l.getLender())).findFirst();

                maybeLoan.ifPresent(l -> {
                    notPreApproved.remove(l);
                    page.add(l);
                    lenders.add(l.getLender());
                });

                keepSearching = !notPreApproved.isEmpty() && maybeLoan.isPresent();
            }

            pages.add(page);
        }

        return pages;
    }
```

### PHP

```
<?php
$pages = buildPages($loans, 3);
printPages($pages);

function buildPages($loans, $pageSize) {

    $pages = array();

    // Sort loans by apr
    usort($loans, function($a, $b) {
        return $a->apr > $b->apr;
    });

    $preApprovedLoans = array();
    $regularLoans = array();

    // Partition loans by pre-approval status
    foreach ($loans as $loan) {
        if ($loan->preApproved) {
            $preApprovedLoans[] = $loan;
        } else {
            $regularLoans[] = $loan;
        }
    }

    // Build pages that have a pre-approved loan
    foreach ($preApprovedLoans as $preApprovedLoan) {
        $pages[] = buildPage($pageSize, $preApprovedLoan, $regularLoans);
    }

    // Process leftover regular loans
    while(count($regularLoans) > 0) {
        $pages[] = buildPage($pageSize, null, $regularLoans);
    }

    return $pages;
}

function buildPage($pageSize, $preApprovedLoan, &$regularLoans) {
    $page = array();
    $lendersOnPage = array();
    if ($preApprovedLoan !== null) {
        $page[] = $preApprovedLoan;
        $lendersOnPage[] = $preApprovedLoan->lender;
    }
    foreach ($regularLoans as $key => $regularLoan) {
        if (count($page) >= $pageSize) {
            break;
        }
        if (!in_array($regularLoan->lender, $lendersOnPage)) {
            $page[] = $regularLoan;
            $lendersOnPage[] = $regularLoan->lender;
            unset($regularLoans[$key]);
        }
    }
    return $page;
}
```
