---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Snow Oni"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/cold
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/oni
  - pf2e/creature/trait/large
statblock: inline
name: "Snow Oni"
level: 13
source: "Monster Core"
aon_id: "creature-3122"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3122"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Snow Oni"
level: "Creature 13"
size: "Large"
trait_01: "Cold"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Oni"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; greater darkvision, snow vision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +24, Athletics +25, Deception +27"
abilityMods: [8, 5, 5, 0, 5, 8]
abilities_top:
  - name: "Snow Vision"
    desc: "Snow doesn't impair the snow oni's vision; they ignore concealment from snowfall."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +25; __Will__: +21"
hp: 290
health:
  - name: "HP"
    desc: "290; __Immunities__ cold; __Weaknesses__ bean panic, spirit 15"
abilities_mid:
  - name: "Bean Panic"
    desc: "Oni are curiously afraid of beans, especially as the seasons begin to change. If a creature Interacts to throw a handful of beans at the oni, the oni becomes frightened 2. While frightened this way, their weakness to spirit damage is increased by 5. The oni then becomes immune to bean panic for 24 hours."
  - name: "Icy Deflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "The snow oni is targeted by a ranged Strike or spell attack roll that doesn't have the fire trait"
  - name: "Effect"
    desc: "The snow oni creates a reflective blockade of ice, gaining a +4 circumstance bonus to AC against the triggering attack roll. If the attack misses, the snow oni redirects the attack to another creature within 20 feet of the snow oni. The attacker rerolls the attack roll against the new target."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +27 (Agile, Magical, reach 10 feet) __Damage__ 2d8+16 bludgeoning plus 2d6 cold"
  - name: "Melee"
    desc: "⬻ jaws +27 (Magical, reach 10 feet) __Damage__ 2d6+16 piercing plus 1d6 persistent bleed"
  - name: "Ranged"
    desc: "⬻ ice dart +25 (Cold, Magical, range increment 60 feet) __Damage__ 3d10+4 cold plus 1d6 spirit"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) The snow oni can take on the appearance of any Medium or Large humanoid creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal"
  - name: "Chilling Combo"
    desc: "⬻ (Cold) The snow oni makes two fist Strikes targeting the same creature. If they both hit, the target becomes slowed 1 for 1 round."
  - name: "Falling Frozen Lightning"
    desc: "⬺ (Cold, Primal) The snow oni calls down a bolt of icy lightning, white as fallen snow. The bolt strikes a location within 60 feet, freezing the air into a cloud of snow that fills a 20-foot burst and lasts for 1 minute. All creatures within the snow become concealed, and all creatures outside the snow become concealed to creatures within it. A creature that enters the snow or begins its turn there takes 15 cold damage, with a DC 33 basic Fortitude save."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 31 - __2nd__ Invisibility (at will; self only)"
sourcebook: "_Monster Core_, page 253."
```

```encounter-table
name: Snow Oni
creatures:
  - 1: Snow Oni
```
