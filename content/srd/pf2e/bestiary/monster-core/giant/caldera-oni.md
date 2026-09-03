---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Caldera Oni"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/oni
  - pf2e/creature/trait/large
statblock: inline
name: "Caldera Oni"
level: 14
source: "Monster Core"
aon_id: "creature-3123"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3123"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Caldera Oni"
level: "Creature 14"
size: "Large"
trait_01: "Fire"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Oni"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +23, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +25, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +27, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +27"
abilityMods: [8, 6, 6, 0, 6, 8]
abilities_top:
  - name: "Items"
    desc: "_+2 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/katana|katana]]_, _+1 [[srd/pf2e/compendium/equipment/runes/resilient-major|resilient]] [[srd/pf2e/compendium/equipment/armor#Breastplate|breastplate]]_"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +28; __Ref__: +25; __Will__: +23"
hp: 315
health:
  - name: "HP"
    desc: "315; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Weaknesses__ bean panic, [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] 15"
abilities_mid:
  - name: "Bean Panic"
    desc: "Oni are curiously afraid of beans, especially as the seasons begin to change. If a creature Interacts to throw a handful of beans at the oni, the oni becomes [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened 2]]. While frightened this way, their weakness to spirit damage is increased by 5. The oni then becomes immune to bean panic for 24 hours."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Stoke the Volcano"
    desc: "When the caldera oni is critically hit, the flames of anger grow within them. They recharge their choice of Ash Form or Dance of Burning War."
speed: "40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _katana_ +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d6+14 slashing plus 2d6 fire"
  - name: "Melee"
    desc: "⬻ jaws +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d6+14 piercing plus 1d8 persistent bleed"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The caldera oni can take on the appearance of any Medium or Large [[srd/pf2e/compendium/rules-elements/traits/player-core/humanoid|humanoid]] creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Ash Form"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]])"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The caldera oni transforms into a cloud of sparking volcanic ash and then Flies. This movement doesn't trigger reactions, and the caldera oni can move through small gaps and spaces occupied by other creatures. The caldera oni then returns to its physical form, affected by a 4th-rank [[srd/pf2e/compendium/spells/rank-2/enlarge|_enlarge_]] spell with a duration of 1d4 rounds."
  - name: "Dance of Burning War"
    desc: "⬽"
  - name: "Frequency"
    desc: "once per minute"
  - name: "Effect"
    desc: "The oni's heat becomes overwhelming, causing them to breathe out superheated ash and dance across the battlefield. The caldera oni Strides, then makes a melee Strike. If the Strike hits, the oni can Stride again and Strike again, repeating this until they have either missed with a Strike or made three Strikes total. The oni then finishes the dance by calling down volcanic lightning through the cloud of ash. Each creature hit by a Strike during the dance takes 3d6 fire damage and 3d6 electricity damage with a DC 34 basic Reflex save."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 34 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only)"
sourcebook: "_Monster Core_, page 254."
```

```encounter-table
name: Caldera Oni
creatures:
  - 1: Caldera Oni
```
