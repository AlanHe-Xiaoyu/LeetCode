# Account Matching

- Maintainer: @preston.guillot

## Overview

This question asks the candidate to implement a semi-realistic business
requirement using a limited data model of displaying the differences between two
sets of account data from credit reports at different points in time for a
single user. The core technical areas tested are basic data structures and
algorithms, but it allows opportunity to explore how a candidate approaches
problem generalization and handling a broader set of concerns.

## Prompts

This problem is presented as a single prompt, given in a format that might
appear in a work ticket:

```
// Given an account defined as:
//
// Account
//   balance (decimal number)
//   name: (string)
//   accountType (e.g. credit card, checking, savings)
//   openedDate: (time stamp)
//
// for example
//   balance: 1000.00
//   name   : Chase Freedom
//   accountType   : credit card
//   opened Date: 6/19/2004
//
// Compare 2 sets of accounts for a user - one set from the current month, and one set from the prior month, e.g.:

// previous: [ { "balance":2000.0, "name":"Chase Freedom", "type":"credit_card", "openedDate":1111680799 }, { "balance":100.0, "name":"Citibank", "type":"credit_card", "openedDate":1000680799 } ]
// current:  [ { "balance":1000.0, "name":"Chase Freedom", "type":"credit_card", "openedDate":1111680799 }, { "balance":500.0, "name":"American Express", "type":"credit_card", "openedDate":1222680799 } ]

//    * print out "<name>: <balance change>" for accounts that are in both months, e.g. "Chase Freedom: -1000"
//    * print out "<name>: added" for those that are in the current month but not the previous month, e.g. "American Express: added"
//    * print out "<name>: deleted" for those that are in the previous month but not the current month, e.g. "Citibank: deleted"
```

This is normally copy/pasted directly into an editor, and the candidate should
be asked to read through the question and encouraged to ask any questions they
might have.

Once the candidate has read through the question, I generally frame the ask in
terms of credit report data to provide some additional context, e.g.

> Imagine a credit report as a snapshot of the data a bureau knows about a user
> at a specific point in time. Just displaying the most current information to a
> user is valuable, but it's more valuable if we can see how a user is trending
> and offer them advice and insights. If a single credit card has a continually
> growing balance, for example, we can offer the user help to re-finance that
> debt and educational materials about credit card debt. If we see that a user
> has a new mortgage, we can congratulate them on buying a new home, and also
> see if we can help them refinance potentially. If a user has a student loan
> account that they've paid off, we can congratulate them on that as well, and
> offer them suggestions on how to maximize their new disposable income etc.

The interviewer should also point out that though the example data is presented
in JSON notation, parsing JSON strings is not a required or expected part of the
solution. Candidates should feel free to create simple classes/structs in their
language of choice that match the data as presented, as if a layer that
de-serializes JSON into it is a given - string parsing isn't a specifically
interesting thing to solve for this problem. A candidate using Javascript (or
any other language that might natively handle JSON) should feel free to start
from the data as-is.

---

#### Expected questions from the candidate

- Types: the candidate should consider the types of all data passed if using a
  statically typed language
  - balance should be any floating point value
  - name should be a simple string
  - account type should ideally be an enum type - in languages where enums are
    not native, a simple string will suffice, but a set of constants is
    preferred
  - opened date should be a date representation that makes sense for the
    platform, e.g. `DateTime` in .Net, `LocalDate` in Java - a simple integer
    timestamp is also fine
- Equality: the candidate should ensure their plan to compare accounts across
  collections makes sense - here the expectation is that an account is "the
  same" if all of name, account type, and opened date are the same between two
  instances, since balance will clearly change report to report
  - it's important that this be done correctly early, if a candidate doesn't
    ask, the interviewer should prompt them to think about it as soon as the
    candidate starts to write equality checks
  - the interviewer should state it's a pre-condition that we can "guarantee"
    that this tuple of three fields _will be_ unique for a given user
- Scale: the candidate should consider how many accounts a user might have, and
  how many users this might be processed for
  - the goal is to get the candidate to do better than a brute force n^2
    solution to this problem - indicate that some users have a surprisingly
    large number of accounts, and we should prefer optimizing time over memory

#### What do we want to see/hear?

- The data structure is a critical component for this problem to not go n^2.
  Good candidates will recognize quickly that a set oriented data structure of
  some sort is required, but many will not think about the need to both check
  for existence by the uniquely identifying tuple _and_ retrieve an item to
  compare balances. A hash map/dictionary is an ideal structure for this
  problem.
  - Easily understandable code should be prioritized as the next most important
    thing to "big-O" run time. Attempts to micro-optimize constant time factors
    that result in harder to understand code are less favorable to a solution
    that includes set oriented logic (e.g. finding "new accounts" is the same as
    finding "removed accounts", with just the order of operands switched as in
    finding set differences)
- Clear modeling: ideally there will be code in an "account" class, and that
  class will know how to determine if two instances of "account" are the same.
  In Java, for example, implementing `equals` and `hashCode` are a standard way
  of doing this.
  - If a candidate implements hash code generation on there own it is a good
    sign, but they might get hung up on the algorithm. It's important they can
    describe the properties of a good hash code (collisions are as infrequent as
    possible, i.e. evenly distributed across the hash space, and that the same
    input always produces the same hash code), but this is an area they can
    choose to implement purposely poorly to not get stuck (e.g. `return 1;`)
- Separation of concerns: the logic to find which accounts are added/new/deleted
  should be cleanly separated from the logic that prints them to the console
- Tests: the prompt contains a data set and the expected output given that data
  set, candidates should at least use this data to ensure their solution works
  as intended - more generalized test cases are always welcome

---

## Options and Additions

There are a couple of possible points of expansion which can be covered for
candidates who move through the question as stated quickly.

### Unknown Output

Ask the candidate to write a solution without knowing ahead of time what the
caller intends to do with the results. Expectations are that the candidate is
able to construct an API that will either return complete enough data that the
user can use all available fields to process results, or the possibility of
allowing a user to pass functions that can be invoked is available.

### Expand the Model

Ask the candidate to think about how they might build a more complete domain
model for "accounts" such that the DTO class directly correlated to the JSON
object isn't necessarily the class operations are being performed on. Ask them
to think about things like how they would display a balance history for an
account that goes back 12 months, assuming that the third party API sent back
the data as presented initially, but they were able to process and store it
before taking further operations.

## Rubric (Coding)

#### Unfamiliar

Positive signs:

- Can correlate accounts
- Can generate a basic report

Negative signs:

- Messy code
- Super slow, ie. double for loop

#### Familiar

Requirements:

- Correctness (can correlate accounts using proper equality checks)

Positive signs:

- Separates correlation from report outputting
- Well-modeled (classes, structs, or other ways of typing or structuring the
  data)
- Avoids `O(N^2)`
- Clean, consistently formatted code
- Takes edge cases into account
- Tests

#### Proficient

Requirements:

- Correctness (can correlate accounts using proper equality checks)
- Separates correlation from report outputting
- Well-modeled (classes, structs, or other ways of typing or structuring the
  data)
- Avoids `O(N^2)`

Positive signs:

- Clean, consistently formatted code
- Takes edge cases into account
- Tests

#### Master

Requirements:

- Correctness (can correlate accounts using proper equality checks)
- Separates correlation from report outputting
- Well-modeled (classes, structs, or other ways of typing or structuring the
  data)
- Avoids `O(N^2)`

Positive signs:

- Solves extensions, either coding or verbally explaining how they would do it
- Discusses performance tradeoffs
- Clean, consistently formatted code
- Takes edge cases into account
- Tests

## Example Solutions

<!-- prettier-ignore -->
### C#

```C#
using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    static void Main(string[] args)
    {
        var previousAccounts = new List<Account>()
        {
            new Account { Balance = 2000, Name = "Chase Freedom", AccountType = AccountType.CREDIT_CARD, OpenedDate = DateTimeOffset.FromUnixTimeSeconds(1111680799) },
            new Account { Balance = 100, Name = "Citibank", AccountType = AccountType.CREDIT_CARD, OpenedDate = DateTimeOffset.FromUnixTimeSeconds(1000680799) },
        };

        var currentAccounts = new List<Account>()
        {
            new Account { Balance = 1000, Name = "Chase Freedom", AccountType = AccountType.CREDIT_CARD, OpenedDate = DateTimeOffset.FromUnixTimeSeconds(1111680799) },
            new Account { Balance = 500, Name = "American Express", AccountType = AccountType.CREDIT_CARD, OpenedDate = DateTimeOffset.FromUnixTimeSeconds(1222680799) },
        };

        //Create dictionaries for both collections, where the key and the value are the same so we can get to the balance later
        var prevAccountsDict = previousAccounts.ToDictionary(x => x, x => x);
        var curAccountsDict = currentAccounts.ToDictionary(x => x, x => x);

        //Use the dictionary key collections (which are really hash sets) to find which accounts are in each of the three required states
        var addedAcccounts = curAccountsDict.Keys.Except(prevAccountsDict.Keys);
        var removedAcccounts = prevAccountsDict.Keys.Except(curAccountsDict.Keys);
        var updatedAccounts = curAccountsDict.Keys.Intersect(prevAccountsDict.Keys);

        //Process each result collection
        foreach(Account account in addedAcccounts) { Console.WriteLine(account.Name + ": added"); }
        foreach(Account account in removedAcccounts) { Console.WriteLine(account.Name + ": deleted"); }
        foreach(Account account in updatedAccounts)
        {
            var currentBalance = curAccountsDict[account].Balance;
            var previousBalance = prevAccountsDict[account].Balance;
            var balanceChange = currentBalance - previousBalance;

            Console.WriteLine(account.Name + ": " + balanceChange);
        }
    }
}

class Account
{
    public decimal Balance { get; set; }
    public string Name { get; set; }
    public AccountType AccountType { get; set;}
    public DateTimeOffset OpenedDate { get; set; }

    public override bool Equals(object obj)
    {
        return Equals(obj as Account);
    }

    public bool Equals(Account other)
    {
        return other != null &&
               this.Name == other.Name &&
               this.AccountType == other.AccountType &&
               this.OpenedDate == other.OpenedDate;
    }

    public override int GetHashCode()
    {
        //Stolen from the internet! https://www.loganfranken.com/blog/692/overriding-equals-in-c-part-2/
        unchecked
        {
            // Choose large primes to avoid hashing collisions
            const int HashingBase = (int)2166136261;
            const int HashingMultiplier = 16777619;

            int hash = HashingBase;
            hash = (hash * HashingMultiplier) ^ this.Name.GetHashCode();
            hash = (hash * HashingMultiplier) ^ this.AccountType.GetHashCode();
            hash = (hash * HashingMultiplier) ^ this.OpenedDate.GetHashCode();

            return hash;
        }
    }
}

enum AccountType
{
    CREDIT_CARD = 1,
    CHECKING = 2,
    SAVING = 3
}
```
