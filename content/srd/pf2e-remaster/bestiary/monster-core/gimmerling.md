---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gimmerling"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/small
statblock: inline
name: "Gimmerling"
level: 12
source: "Monster Core"
aon_id: "creature-3018"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3018"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gimmerling"
level: "Creature 12"
size: "Small"
trait_01: "Fey"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; hungersense (imprecise) 30 feet, low-light vision"
languages: "Aklo, Common, Fey"
skills:
  - name: "Skills"
    desc: "Athletics +22, Crafting +23, Deception +25, Nature +21, Stealth +25, Thievery +25"
abilityMods: [4, 7, 4, 5, 3, 4]
abilities_top:
  - name: "Hungersense"
    desc: "The gimmerling senses creatures that require food to live."
  - name: "Items"
    desc: "_+1 striking hand crossbow_ (20 bolts)"
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +22; __Ref__: +25; __Will__: +19"
hp: 235
health:
  - name: "HP"
    desc: "235; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Treacherous Aura"
    desc: "(aura, primal) 15 feet. Tangled roots, jagged divots, sharp rocks and other hazards appear on surfaces in the aura, creating difficult terrain."
  - name: "Trip Up"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature critically fails a melee attack to hit the gimmerling or moves into a space within the gimmerling's treacherous aura"
  - name: "Effect"
    desc: "The triggering creature must attempt a DC 32 Reflex save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target is off-guard until the start of its next turn."
  - name: "Failure"
    desc: "The target takes 2d10 bludgeoning damage and is off-guard until the start of its next turn."
  - name: "Critical Failure"
    desc: "As failure, and the target is knocked prone."
speed: "30 feet; trickster's step"
attacks:
  - name: "Melee"
    desc: "⬻ claw +26 (Agile, Finesse) __Damage__ 2d8+7 slashing plus Sly Disarm"
  - name: "Melee"
    desc: "⬻ jaws +26 (Finesse) __Damage__ 3d8+7 piercing plus 2d6 poison"
  - name: "Ranged"
    desc: "⬻ hand crossbow +28 (range increment 60 feet, reload 1) __Damage__ 2d6+3 piercing plus 2d6 poison"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) The gimmerling takes on the appearance of any humanoid. In humanoid form, They lose their treacherous aura, and their equipment appears to be trinkets or toys. If the chosen form lacks claws or fangs, they lose the matching Strike. If they lose their claw Strike, they gain a fist Strike that is identical except that it deals bludgeoning damage."
  - name: "Sly Disarm"
    desc: "⬻"
  - name: "Requirements"
    desc: "The gimmerling's last action was a successful claw Strike"
  - name: "Effect"
    desc: "The gimmerling attempts to Disarm the creature they hit. They gain a +4 status bonus on the Athletics check. This attempt neither applies nor counts toward the gimmerling's multiple attack penalty."
  - name: "Sneak Attack"
    desc: "The gimmerling deals 2d6 extra precision damage to off-guard creatures."
  - name: "Trickster's Step"
    desc: "The gimmerling ignores difficult terrain and doesn't trigger traps with their movement. Gimmerling Keepsakes Gimmerlings collect weapons, traps, mechanical novelties, and dangerous magic items. A gimmerling is likely found with toolkits (like artisan's toolkits, repair toolkits, and thieves' toolkits) and items it can use to appear more vulnerable, such as locks, manacles, and snare kits (which it feigns being trapped by). Hunting Grounds Gimmerlings are more common in the First World than in the Universe proper and favor hunting grounds on the verges of dangerous places where they might encounter protective creatures to mislead with their disguises."
sourcebook: "_Monster Core_, page 170."
```

```encounter-table
name: Gimmerling
creatures:
  - 1: Gimmerling
```
