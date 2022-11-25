<h1 align="center">Gobot</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/LuckMeelo/gobot?color=fb8500">

  <!-- <img alt="Github language count" src="https://img.shields.io/github/languages/count/LuckMeelo/gobot?color=56BEB8"> -->

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/LuckMeelo/gobot?color=f15bb5">

  <img alt="License" src="https://img.shields.io/github/license/LuckMeelo/gobot?color=80b918">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/gobot?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/gobot?color=56BEB8" /> -->

  <img alt="Github stars" src="https://img.shields.io/github/stars/LuckMeelo/gobot?color=56BEB8" /> 
</p>


---

<p align="center"> A simple Gomoku Bot
    <br> 
</p>

## 📝 Table of Contents

- [Table of Contents](#-table-of-contents)
- [About ](#-about-)
- [Getting Started ](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Build](#build)
- [Running the tests ](#-running-the-tests-)
- [Usage ](#-usage-)

## 🧐 About <a name = "about"></a>

A [Gomoku Narabe game](https://en.wikipedia.org/wiki/Gomoku) bot (also called Wuzi Qi, Slope, Darpion or Five in a Row), focusing on the performance of its artificial intelligence.
This bot is compliant with [Piskvork's communication protocol](https://plastovicka.github.io/protocl2en.htm).

## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites

What things you need to install the software and how to install them.

- [Python and Pip](https://www.python.org/) Version >= 3.0
- [Piskvork](https://sourceforge.net/projects/piskvork/) The Gomoku Game manager used

### Build

- Windows
  Generate the pbrain-gomoku-ai.exe with
```
python3 compile.py
```
- Linux
  Generate the pbrain-gomoku-ai binary with
```
make
```

## 🔧 Running the tests <a name = "tests"></a>

To run tests you need to install [pytest](https://docs.pytest.org/en/7.2.x/) and use:

```
make tests_run
```

## 🎈 Usage <a name="usage"></a>

- Run the Piskvork manager
- Build the project and add the pbrain-gomoku-ai.exe file as a player.

Made with :heart: by <a href="https://github.com/LuckMeelo" target="_blank">LuckMeelo</a>