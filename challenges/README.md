# Daily Challenges

This part of the course puts the earlier Python lessons into practice through daily projects. Use this README as the index for challenge groups; each group's README contains the project explanations, examples, and running instructions.

**Status: in progress.** Days 1–8 are currently implemented and documented.

## Learning order

1. Work through the numbered lesson folders up to `11_exceptions`.
2. Complete challenges in day order, starting with `day [1-11]` and continuing through the groups listed below.
3. After all challenge groups, continue with the next numbered course section (`12_...`, when added).

Follow this order even if your editor sorts the folders differently.

## Challenge groups

| Folder | Current coverage | Status |
| --- | --- | --- |
| [day 1–11](day%20%5B1-11%5D/README.md) | Days 1–8 | In progress |
| `day [12-21]` | Reserved for later challenges | Planned |
| `day [22-31]` | Reserved for later challenges | Planned |
| `day [32-35]` | Reserved for later challenges | Planned |
| `day [36-45]` | Reserved for later challenges | Planned |
| `day [46-52]` | Reserved for later challenges | Planned |

## Projects covered so far

| Day | Project | Main concepts |
| --- | --- | --- |
| 1 | [Self-Intro Script Generator](day%20%5B1-11%5D/README.md#day-1-self-intro-script-generator) | `input()`, `.strip()`, f-strings, the current date, and a decorative text border. |
| 2 | [Stylish Bio Generator](day%20%5B1-11%5D/README.md#day-2-stylish-bio-generator) | Functions, conditional layouts, emojis, `textwrap.dedent()`, and optional UTF-8 text file output. |
| 3 | [Simple Bill Splitter](day%20%5B1-11%5D/README.md#day-3-simple-bill-splitter) | Lists, loops, numeric conversion, retrying input with `ValueError`, division, and `round()`. |
| 4 | [Minutes Alive Calculator](day%20%5B1-11%5D/README.md#day-4-minutes-alive-calculator) | Functions, numeric conversion, tuple unpacking, rounding, and repeated calculations. |
| 5 | [Emoji Enhancer for Messages](day%20%5B1-11%5D/README.md#day-5-emoji-enhancer-for-messages) | Dictionaries, `.get()`, string cleanup, loops, and joining words into an enhanced message. |
| 6 | [Daily Learning Journal Logger](day%20%5B1-11%5D/README.md#day-6-daily-learning-journal-logger) | Timestamps, optional input, UTF-8 file output, append mode, and paths relative to the script. |
| 7 | [Terminal-Based Task List Manager](day%20%5B1-11%5D/README.md#day-7-terminal-based-task-list-manager) | Functions, lists of dictionaries, `match`, input validation, and persistent task storage. |
| 8 | [Password Strength Checker & Suggestion Tool](day%20%5B1-11%5D/README.md#day-8-password-strength-checker-and-suggestion-tool) | Hidden input with `getpass`, character checks with `any()`, and random password suggestions. |

## Original challenge statements

The `DAY_*.md` files contain the original task descriptions and are maintained manually by the repository owner. Preserve their original wording when working on solutions or documentation. Project explanations, running instructions, and progress belong in README files.

As new days are added, update the relevant group's README and this index to reflect the actual content.

## Running the projects

From the repository root, choose the command for the project you want to run:

```powershell
python "challenges/day [1-11]/day_1.py"
python "challenges/day [1-11]/day_2.py"
python "challenges/day [1-11]/day_3.py"
python "challenges/day [1-11]/day_4.py"
python "challenges/day [1-11]/day_5.py"
python "challenges/day [1-11]/day_6.py"
python "challenges/day [1-11]/day_7.py"
python "challenges/day [1-11]/day_8.py"
```

The quotes keep the path's spaces and square brackets together. Answer each prompt in the terminal and press **Enter** to continue.

In VS Code, open the Python file and press **Ctrl + S** to format and run it. Click inside the Run on Save terminal to enter your answers. See the [group README](day%20%5B1-11%5D/README.md#how-to-run-these-projects) for detailed examples, including where Days 2, 6, and 7 save their files.

Day 8 hides password input: type in the terminal and press **Enter**, even though no characters or stars appear.

See the [main README](../README.md#folder-overview) for the overall course structure and [editor setup](../README.md#quick-start).
