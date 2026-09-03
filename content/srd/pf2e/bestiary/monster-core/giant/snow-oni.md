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
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +24, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +25, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +27"
abilityMods: [8, 5, 5, 0, 5, 8]
abilities_top:
  - name: "Snow Vision"
    desc: "Snow doesn't impair the snow oni's vision; they ignore [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealment]] from snowfall."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +23; __Ref__: +25; __Will__: +21"
hp: 290
health:
  - name: "HP"
    desc: "290; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]]; __Weaknesses__ bean panic, spirit 15"
abilities_mid:
  - name: "Bean Panic"
    desc: "Oni are curiously afraid of beans, especially as the seasons begin to change. If a creature Interacts to throw a handful of beans at the oni, the oni becomes [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 2]]. While frightened this way, their weakness to spirit damage is increased by 5. The oni then becomes immune to bean panic for 24 hours."
  - name: "Icy Deflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "The snow oni is targeted by a ranged Strike or spell attack roll that doesn't have the [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] trait"
  - name: "Effect"
    desc: "The snow oni creates a reflective blockade of ice, gaining a +4 circumstance bonus to AC against the triggering attack roll. If the attack misses, the snow oni redirects the attack to another creature within 20 feet of the snow oni. The attacker rerolls the attack roll against the new target."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+16 bludgeoning plus 2d6 cold"
  - name: "Melee"
    desc: "⬻ jaws +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+16 piercing plus 1d6 persistent bleed"
  - name: "Ranged"
    desc: "⬻ ice dart +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 60 feet) __Damage__ 3d10+4 cold plus 1d6 spirit"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The snow oni can take on the appearance of any Medium or Large [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]] creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal"
  - name: "Chilling Combo"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]]) The snow oni makes two fist Strikes targeting the same creature. If they both hit, the target becomes [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for 1 round."
  - name: "Falling Frozen Lightning"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/cold|Cold]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The snow oni calls down a bolt of icy lightning, white as fallen snow. The bolt strikes a location within 60 feet, freezing the air into a cloud of snow that fills a 20-foot burst and lasts for 1 minute. All creatures within the snow become [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealed]], and all creatures outside the snow become concealed to creatures within it. A creature that enters the snow or begins its turn there takes 15 cold damage, with a DC 33 basic Fortitude save."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 31 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only)"
sourcebook: "_Monster Core_, page 253."
```

```encounter-table
name: Snow Oni
creatures:
  - 1: Snow Oni
```
