---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Halfling Head Chef"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/halfling
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Halfling Head Chef"
level: 2
source: "NPC Core"
aon_id: "creature-3644"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3644"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Halfling Head Chef"
level: "Creature 2"
size: "Small"
trait_01: "Halfling"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; (15 to smell and taste) keen eyes, scent (imprecise) 30 feet"
languages: "Common, Halfling"
skills:
  - name: "Skills"
    desc: "Acrobatics +7, Baking Lore +15, Cooking Lore +17, Intimidation +7, Society +6"
abilityMods: [1, 3, 2, 2, 1, 1]
abilities_top:
  - name: "Culinary Specialist"
    desc: "For encounters involving cooking and taste, the head chef is a 7th-level challenge."
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the Seek action to find hidden or undetected creatures within 30 feet of them. Whenever the halfling targets a creature that is concealed or hidden from them, reduce the DC of the flat check to 3 for a concealed target or 9 for a hidden one."
  - name: "Items"
    desc: "chef's hat, Filcher's Fork, Frying Pan, herbs and spices"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +7; __Will__: +7"
hp: 36
health:
  - name: "HP"
    desc: "36"
abilities_mid:
  - name: "Dash of Spice"
    desc: "⬲"
  - name: "Trigger"
    desc: "The head chef is targeted with a melee attack by an adjacent attacker they can see"
  - name: "Effect"
    desc: "The head chef uses Spice Mix against the attacker."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hot frying pan +9 (fatal d8) __Damage__ 1d4+3 bludgeoning plus 1d4 fire"
  - name: "Melee"
    desc: "⬻ filcher's fork +9 (Agile, Backstabber, deadly d6) __Damage__ 1d4+3 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+3 bludgeoning"
  - name: "Ranged"
    desc: "⬻ filcher's fork +9 (Agile, Backstabber, deadly d6, thrown 20 feet) __Damage__ 1d4+3 piercing"
abilities_bot:
  - name: "Angry Rant"
    desc: "⬻ (Auditory, Emotion, Linguistic, Mental)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The chef shouts a flurry of insults and criticisms at either an ally or enemy within 30 feet with the following effects:"
  - name: "Ally"
    desc: "The chef's assistant is shaken by the barrage of criticism but is determined to work faster and harder. The target becomes quickened for 1 round but is also frightened 1. They can use the extra action to Interact, Step, or Stride, or as part of an action or activity to prepare, cook, or serve food."
  - name: "Enemy"
    desc: "The target must succeed a DC 18 Will save or take 1d6 mental damage and become frightened 1 (or 2d6 mental damage and frightened 2 on a critical failure)."
  - name: "Spice Mix"
    desc: "⬻ The head chef throws a mixture of irritating spices into an adjacent creature's eyes, causing the creature to be dazzled until it Interacts to clear its vision. Chef's Menu A halfling head chef crafts exquisite dishes that tantalize the taste buds. Delights like honeyblossom pudding (honey, cream, and flower petals), stuffed burrow rolls (meat and vegetables wrapped in flaky pastry), sunberry glazed roast (meat marinated in sunberry sauce), and root medley gratin (layers of root vegetables and cheese) showcase their prowess."
sourcebook: "_NPC Core_, page 190."
```

```encounter-table
name: Halfling Head Chef
creatures:
  - 1: Halfling Head Chef
```
