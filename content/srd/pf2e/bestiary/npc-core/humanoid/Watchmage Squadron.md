---
noteType: pf2eMonster
aliases: "Watchmage Squadron"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Watchmage Squadron"
level: 10
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3567"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Watchmage Squadron"
level: "Creature 10"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 22
perception:
  - name: "Perception"
    desc: "+22; invisibility scan"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +21, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +19, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +20, [[srd/pf2e/compendium/rules-elements/skills/Lore|Legal Lore]] +21, [[srd/pf2e/compendium/rules-elements/skills/Society|Society]] +19"
abilityMods: [3, 4, 3, 5, 2, 0]
abilities_top:
  - name: "Invisibility Scan"
    desc: "Invisibility can't make anything [[srd/pf2e/compendium/rules-elements/Conditions#Undetected|undetected]] or [[srd/pf2e/compendium/rules-elements/Conditions#Unnoticed|unnoticed]] to the watchmage squadron."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +22; __Ref__: +16; __Will__: +19"
hp: 180
health:
  - name: "HP"
    desc: "180 (4 segments); __Weaknesses__ area damage 10, [[srd/pf2e/compendium/rules-elements/traits/gm-core/Splash|splash]] damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet, troop movement"
abilities_bot:
  - name: "Troop Spellcasting"
    desc: "When the watchmage squadron Casts a Spell, the individual members combine their efforts into casting a more powerful version than any one member could achieve alone. When Casting a Spell that has an area of a burst, cone, or line and doesn't have a duration, increase the area of that spell. Add 5 feet to the radius of a burst that normally has a radius of at least 10 feet (a burst with a smaller radius is not affected). Add 5 feet to the length of a cone or line that is normally 15 feet long or smaller, and add 10 feet to the length of a larger cone or line."
  - name: "Bash Heads"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]]) The watchmages lash out against all enemies in a 5-foot emanation with their fists, dealing 4d4+4 bludgeoning damage with a DC 29 basic Reflex save. __Fire Shortbows!__ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|Arcane]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The watchmages fire a volley against each enemy in a 10-foot burst within 150 feet, with a DC 26 basic Reflex save. The damage depends on the number of actions. When the squadron is reduced to 2 or fewer segments, this area decreases to a 5-foot burst. ⬻ 1d6+3 piercing plus 1d6 force damage ⬺ 3d6+6 piercing plus 1d6 force damage ⬽ 4d6+6 piercing plus 1d6 force damage"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 26, attack +18 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Frostbite|Frostbite]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Tangle Vine|Tangle Vine]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Revealing Light|Revealing Light]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-1/Grim Tendrils|Grim Tendrils]] - __5th__ [[srd/pf2e/compendium/spells/rank-3/Fireball|Fireball]], [[srd/pf2e/compendium/spells/rank-3/Locate|Locate]], [[srd/pf2e/compendium/spells/rank-5/Slither|Slither]]"
sourcebook: "_NPC Core_, page 120."
```

```encounter-table
name: Watchmage Squadron
creatures:
  - 1: Watchmage Squadron
```
