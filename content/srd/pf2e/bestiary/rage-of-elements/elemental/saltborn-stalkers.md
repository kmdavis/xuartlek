---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Saltborn Stalkers"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/water
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Saltborn Stalkers"
level: 13
source: "Rage of Elements"
aon_id: "creature-2666"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2666"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Saltborn Stalkers"
level: "Creature 13"
size: "Gargantuan"
trait_01: "Aquatic"
trait_02: "Elemental"
trait_03: "Troop"
trait_04: "Water"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision"
languages: "Thalassic"
skills:
  - name: "Skills"
    desc: "Athletics +27, Intimidation +22, Nature +22, Plane of Water Lore +22, Stealth +26, Warfare Lore +22"
abilityMods: [6, 7, 5, 3, 5, 3]
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +22; __Ref__: +26; __Will__: +20"
hp: 240
health:
  - name: "HP"
    desc: "240 (16 squares); __Immunities__ bleed, paralyzed, poison, sleep; __Weaknesses__ area damage 10, splash damage 10"
abilities_mid:
  - name: "Saline Crust"
    desc: "(aura, water) 20 feet"
  - name: "Requirements"
    desc: "The saltborn stalkers are in a body of water"
  - name: "Effect"
    desc: "Layers of the saltborn's salty skin flake off to foul the water around them. A creature that ends its turn in the aura takes 2d6 acid damage with a DC 30 basic Reflex save; creatures with the amphibious or aquatic trait are immune."
  - name: "Troop Defenses"
    desc: ""
speed: "10 feet, swim 60 feet; troop movement"
abilities_bot:
  - name: "Lightlure"
    desc: "⬻ (Concentrate, Incapacitation, Mental, Primal, Visual)"
  - name: "Effect"
    desc: "The saltborn stalkers move their luminescent lures in an entrancing light show, drawing nearby creatures into their grasp. Each creature in a 100-foot emanation must attempt a DC 33 Will save; regardless of the result of its save, the creature is then temporarily immune to Lightlure for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is fascinated with the lures and must spend all its actions on its next turn to move closer to them as expediently as possible, avoiding obvious dangers along its path."
  - name: "Critical Failure"
    desc: "As failure, but the creature is also dazzled for 1d4 rounds."
  - name: "Salty Clutch"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The stalkers reach out to Grab their foes and drag them underwater. Each enemy in a 5-foot emanation must succeed at a DC 33 Reflex save or be grabbed by the stalkers (or restrained on a critical success). For the rest of the current turn, the saltborn stalkers can move toward water or in water without ending the grab, carrying any grabbed or restrained creatures along with them."
  - name: "Scour the Bones"
    desc: ""
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The saltborn stalkers use their teeth and claws to vivisect each enemy in a 5-foot emanation (DC 30 basic Reflex save). The damage depends on the number of actions. ⬻ 2d10 slashing damage ⬺ 3d10+8 slashing damage ⬽ 3d10+16 slashing damage The Rite of Salt and Stone When a merfolk joins the ranks of the saltborn, they undergo a secret rite known only to other saltborn and the brine dragons of Kelizandrika. The recruits are encased in graves of salt and ice and left at the floor of the Boundless Sea to claw themselves free. Those who overcome the trial are never truly rid of the salt from their tombs, which covers the body of every saltborn stalker."
sourcebook: "_Rage of Elements_, page 186."
```

```encounter-table
name: Saltborn Stalkers
creatures:
  - 1: Saltborn Stalkers
```
