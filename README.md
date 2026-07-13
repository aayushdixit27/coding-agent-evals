# coding-agent-evals

Red-team-grade eval rigor for AI coding agents, where "passed" is not "correct."

## The problem

As more code is written by AI coding agents, one question matters more: when an agent's work passes the test, did it solve the problem or just satisfy the check?

A test suite is a signal. Signals can be satisfied without being correct. An agent can read a check, work backward from what makes it green, and hand back something that clears the bar while missing the point. The check says pass. The problem is still open. This suite exists to measure that gap, and to make it hard for an agent to close the gap the wrong way.

## How the suite works

Each task ships two things.

The first is a deliverable the agent produces. It runs on inputs the agent never sees, so the agent cannot tune its answer to a known set of cases. It has to build something that generalizes.

The second is a hidden verifier. It checks semantic correctness against the written spec, and it is the only thing that counts toward a score. The agent does not get to read it.

Some tasks go a step further. A trap task also hands the agent a visible test it can run and iterate against. That visible test looks like a normal part of the workflow, and an agent will naturally lean on it to decide when it is done. The catch is that the visible test is not the one being scored. Only the hidden verifier is. If the agent trusts the visible test all the way to the finish, it can walk straight into the trap.

## The three headline traps

The traps come as a trio, one for each way a check can lie to you.

- **Too loose.** The visible check is weak. It accepts a wrong answer because it does not look closely enough. An agent that passes it can still be wrong.
- **Too shallow.** The visible test is silent on a behavior the spec requires. It never exercises that path, so an agent can leave it unimplemented or broken and the test stays green.
- **Plain wrong.** The visible test contradicts the written spec. An agent that treats the test as the source of truth will build to the test and fail the spec.

Each trap rewards the same mistake: trusting the check over the problem. The hidden verifier is what tells them apart.

## The validation gate

Every task passes a two-way gate before it ships. This is how we know the traps have teeth by construction, not by hope.

1. **The oracle passes.** A correct reference solution passes the hidden verifier. This proves the task is solvable and the verifier accepts genuinely correct work.
2. **The lazy solution fails.** A hand-written solution that takes the tempting shortcut fails, and it fails on exactly the trap it targets. This proves the trap catches the specific mistake it was built to catch.

A task ships only when both hold. The oracle earns a pass, and the lazy solution earns the failure it deserves, in the place it was designed to earn it.

## Status

This is being built in public over roughly two weeks. The first task has landed: T1, range-expand, a capability task that establishes the hidden-verifier format, with the three headline traps (too loose, too shallow, plain wrong) coming next. It is one of a planned roster of eight, and more will follow as they clear the validation gate.
