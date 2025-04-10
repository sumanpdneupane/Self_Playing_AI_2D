### Self-Playing AI 2D - An AI that plays 2D games without human input.
```
Self-Playing AI 2D is an autonomous 2D game-playing AI that learns and 
improves its gameplay using Genetic Algorithms (GA). Unlike rule-based or 
hardcoded bots, Self-Playing AI 2D evolves by observing the game screen, 
making decisions, and refining its strategy over multiple generations.

The AI can play any 2D game that can be controlled using a keyboard and 
mouse, such as Snake, Flappy Bird, or Car Racing, without needing APIs or 
predefined game rules.

This allows the AI to learn from scratch and adapt to any 2D game, even if 
it has never seen it before. Over time, it will improve its decision-making 
by recognizing patterns and optimizing its actions to maximize rewards across 
different game types.
```

### Flexible game-playing AI: adapting to multiple games and 
### board sizes (Survival Of the Fitness)
```
https://arxiv.org/html/2408.13871v1
```

### Game Play Design
```
self_playing_ai_2d/
│
├── main.py                 # Entry point
├── screen_capture.py       # Capture screen
├── input_controller.py     # Keyboard/mouse control
├── game_decision_agent.py  # Agent brain and decision logic "What should I do right now?"
├── genetic_algorithm.py    # GA loop “How do I get better over time?"
└── utils.py                # Misc helpers

```

### How to Run Game
```
Coming soon
``