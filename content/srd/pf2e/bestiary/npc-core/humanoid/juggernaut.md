---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Juggernaut"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/large
statblock: inline
name: "Juggernaut"
level: 13
source: "NPC Core"
aon_id: "creature-3465"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3465"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Juggernaut"
level: "Creature 13"
size: "Large"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +26, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +26, [[srd/pf2e/compendium/rules-elements/skills/lore|Engineering Lore]] +24"
abilityMods: [8, 3, 4, 2, 2, 2]
abilities_top:
  - name: "Integrated Weapon"
    desc: "A juggernaut's armor includes one integrated melee weapon, such as a diamond-tipped rotary saw blade, massive pneumatic drill, or heavy spiked gauntlet. The specifics don't change the damage dealt by its Strikes, but determines whether it deals bludgeoning, piercing, or slashing damage. A juggernaut with tools and a workshop can spend 2 hours to swap their armor's integrated weapon."
  - name: "Power Source"
    desc: "Juggernaut armor requires a power source built into the armor—such as a steam boiler, Stasian coil, or alchemical reservoir. This determines a damage type—cold, electricity, fire, or poison—for certain abilities."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/adventuring-gear/artisans-toolkit-sterling|Artisan's Toolkit]] (blacksmithing), juggernaut armor, [[srd/pf2e/compendium/equipment/adventuring-gear/repair-toolkit-superb|Repair Toolkit]]"
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +25; __Ref__: +19; __Will__: +21"
hp: 250
health:
  - name: "HP"
    desc: "250; __Resistances__ galvanized plating"
abilities_mid:
  - name: "Galvanized Plating"
    desc: "The juggernaut has resistance 10 to the damage type of the armor's power source."
  - name: "Self-Destruct"
    desc: "⬲"
  - name: "Trigger"
    desc: "The juggernaut is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "The juggernaut collapses and their armor emits a steady ticking sound. At the beginning of what would have been the juggernaut's next turn, the armor's power source explodes, destroying it completely and dealing 10d6 damage in a 30-foot emanation with a DC 33 basic Reflex save. The explosion deals the damage type of the armor's power source. An adjacent creature can cancel the self-destruct sequence by succeeding at a DC 31 [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] check to [[srd/pf2e/compendium/rules-elements/actions/player-core#Disable a Device|Disable a Device]]."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ integrated weapon +27 __Damage__ 3d8+12 and see integrated weapon"
  - name: "Melee"
    desc: "⬻ plated fist +27 __Damage__ 3d4+14 bludgeoning"
abilities_bot:
  - name: "Energy Projector"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/alchemical|Alchemical]]) A juggernaut carries a powerful cannon-like projectile weapon that requires two hands to wield and deals 14d6 damage to all creatures in its area with a DC 31 basic save; the damage type, area, and save are based on the armor's power source, as listed below. Once activated, Energy Projector can't be used again for 1d4 rounds."
  - name: "Cold"
    desc: "30-foot cone of cold (Reflex)"
  - name: "Electricity"
    desc: "60-foot line of electricity (Reflex)"
  - name: "Fire"
    desc: "30-foot cone of fire (Reflex)"
  - name: "Poison"
    desc: "30-foot cone of poison gas (Fortitude)"
  - name: "Jump Jets"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/alchemical|Alchemical]]) The juggernaut gains a Fly speed of 15 feet until the end of their current turn. If the juggernaut isn't on solid ground when they lose their fly Speed, they fall. After the effect ends, the juggernaut can't use Jump Jets again for 1 round."
  - name: "Trample"
    desc: "⬽ Medium or smaller, plated fist, DC 33 Juggernaut Rumors Legend has it that the first suit of juggernaut armor was built by a brilliant but misanthropic inventor who leveled his own workshop before embarking on a spree of indiscriminate destruction. Though the rampage quickly came to an end when his creation crashed through a wooden floor and became trapped in a basement, the story has inspired a new generation of machinists to diligently refine and improve on the original design."
sourcebook: "_NPC Core_, page 49."
```

```encounter-table
name: Juggernaut
creatures:
  - 1: Juggernaut
```
