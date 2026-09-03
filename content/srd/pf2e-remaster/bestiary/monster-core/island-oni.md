---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Island Oni"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/oni
  - pf2e/creature/trait/water
  - pf2e/creature/trait/huge
statblock: inline
name: "Island Oni"
level: 17
source: "Monster Core"
aon_id: "creature-3124"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3124"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Island Oni"
level: "Creature 17"
size: "Huge"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Oni"
trait_04: "Water"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32; greater darkvision, mist vision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +30, Athletics +33, Deception +32, Intimidation +32, Nature +29"
abilityMods: [9, 6, 6, 2, 9, 6]
abilities_top:
  - name: "Mist Vision"
    desc: "The island oni ignores the concealed condition from fog and mist."
  - name: "Items"
    desc: "_+2 greater striking longspear_"
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +26; __Ref__: +28; __Will__: +34 +1 status on all saves vs. water"
hp: 390
health:
  - name: "HP"
    desc: "390; __Immunities__ electricity; __Weaknesses__ bean panic, spirit 20"
abilities_mid:
  - name: "Bean Panic"
    desc: "Oni are curiously afraid of beans, especially as the seasons begin to change. If a creature Interacts to throw a handful of beans at the oni, the oni becomes frightened 2. While frightened this way, their weakness to spirit damage is increased by 5. The oni then becomes immune to bean panic for 24 hours."
  - name: "Lost Oni Island"
    desc: "(aura, primal) An island oni can claim an island of up to 1-mile radius in a process that takes 1 week, during which the oni must defeat any who come to challenge its claim. If successful, the oni can freely control the weather on its island and in a 1-mile radius from the shore, with the effect of a successful _control weather_ ritual. This altered weather surrounds the island in thick fog, seaborne mirages, or other phenomena that increase the DC of checks to locate and navigate to the island (Such as Sailing Lore or Survival) to 40, though the oni can allow allies to pass freely. If the oni dies or leaves the island, the weather returns to normal immediately."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, fly 40 feet, swim 50 feet; water walk"
attacks:
  - name: "Melee"
    desc: "⬻ _longspear_ +35 (Magical, reach 20 feet) __Damage__ 3d8+10 piercing plus 2d6 electricity"
  - name: "Melee"
    desc: "⬻ jaws +33 (Magical, reach 15 feet) __Damage__ 3d6+10 piercing plus 2d6 persistent electricity and Improved Grab"
  - name: "Ranged"
    desc: "⬻ thunderbolt +30 (Electricity, Magical, range increment 60 feet) __Damage__ 3d12+12 electricity plus off-guard for 1 round"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, Primal) The island oni can take on the appearance of any Medium or Large humanoid creature. This doesn't change their Speed or their attack and damage bonuses with their Strikes but might change the damage type their Strikes deal (typically to bludgeoning)."
  - name: "Conductive Downpour"
    desc: "⬺ (Electricity, Primal, Water) The island oni fires a bolt of lightning into the air, which immediately roils with dark clouds. Rain falls in a 60-foot radius emanation, centered on the oni, for 1 minute, filling the air and pooling on the ground. Creatures in the aura gain weakness 10 to electricity, and the entire area is greater difficult terrain for Flying creatures, and difficult terrain for creatures on the ground or Climbing, unless they also have a swim Speed."
  - name: "Electrifying Pierce"
    desc: "⬻ (Electricity, Primal)"
  - name: "Requirements"
    desc: "The island oni's last action was a successful longspear Strike against a Medium or smaller target"
  - name: "Effect"
    desc: "The island oni drives the spear through the target and calls lightning to strike the spear. The target takes 6d6 electricity damage with a DC 37 basic Fortitude save. On a failure, the creature is also impaled on the spear. It's grabbed, and if the oni moves, they bring the grabbed creature along with them. The island oni doesn't need to use additional actions to keep the creature grabbed; the creature remains grabbed as long as it's impaled. The grabbed creature can attempt to Escape as normal. The island oni can only have one creature impaled this way at a time."
  - name: "Swallow Whole"
    desc: "⬻ medium, 3d8+10 bludgeoning, Rupture 30"
  - name: "Tripping Tide"
    desc: "⬺ (Water) The island oni sweeps their spear in a full circle, releasing waves of seawater. All creatures in a 20-foot emanation must succeed a DC 37 Reflex Saving throw or fall prone."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 37 2nd invisibility (at will, self only) - __Constant (9th)__ Water Walk"
sourcebook: "_Monster Core_, page 254."
```

```encounter-table
name: Island Oni
creatures:
  - 1: Island Oni
```
