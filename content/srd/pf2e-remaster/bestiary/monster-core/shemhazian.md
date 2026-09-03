---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shemhazian"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Shemhazian"
level: 16
source: "Monster Core"
aon_id: "creature-2900"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2900"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Shemhazian"
level: "Creature 16"
size: "Gargantuan"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision, scent (imprecise) 60 feet, _truesight_"
languages: "Chthonian, Draconic, Empyrean; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +31, Deception +25, Intimidation +27, Medicine +28, Religion +30"
abilityMods: [9, 5, 7, 0, 6, 3]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +32; __Ref__: +26; __Will__: +27 +1 status to all saves vs. magic"
hp: 350
health:
  - name: "HP"
    desc: "350; __Weaknesses__ cold iron 15, holy 15"
abilities_mid:
  - name: "Paralyzing Gaze"
    desc: "(aura, divine, unholy, visual) 30 feet. A non-demon creature that ends its turn in the aura must attempt a DC 35 Fortitude save. If it fails, it's slowed 1 for 1 round, and if it critically fails, it is paralyzed for 1 round."
  - name: "Succor Vulnerability"
    desc: "A shemhazian's mutilation is a part of them, and they can't bear to see it reversed. The first time each round that a creature heals from damage the shemhazian dealt on their last turn, the demon takes 3d6 mental damage."
  - name: "Tail Whip"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within reach of the shemhazian's tail leaves a square during a move action it's using"
  - name: "Effect"
    desc: "The shemhazian attempts to Trip the triggering creature. On a success, the creature also takes damage as if the shemhazian had hit with a tail Strike, and if the creature was flying, it falls 30 feet."
speed: "35 feet, climb 20 feet, fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +33 (Magical, reach 20 feet, Unholy) __Damage__ 3d12+17 piercing plus enfeebling bite"
  - name: "Melee"
    desc: "⬻ claw +33 (Agile, Magical, reach 20 feet, Unholy) __Damage__ 3d8+17 slashing"
  - name: "Melee"
    desc: "⬻ pincer +33 (Magical, reach 20 feet, Unholy) __Damage__ 3d8+17 bludgeoning plus Improved Grab"
  - name: "Melee"
    desc: "⬻ tail +33 (Magical, reach 30 feet, Unholy) __Damage__ 3d8+17 slashing"
abilities_bot:
  - name: "Enfeebling Bite"
    desc: "(Divine) If the shemhazian's jaws Strike damages a creature, the target is enfeebled 3 for 24 hours. The target can attempt a DC 37 Fortitude save to reduce this to enfeebled 1 (or be unaffected on a critical success)."
  - name: "Focused Gaze"
    desc: "⬻ (Concentrate, Divine, Incapacitation, Visual) The shemhazian focuses their gaze on a non-demon creature they can see within 30 feet. If that creature isn't already slowed by the shemhazian's paralyzing gaze, it must attempt a save against the shemhazian's paralyzing gaze. If that creature is slowed, it must succeed at a DC 35 Fortitude save or be paralyzed for 1 round. A shemhazian can't use this ability against the same creature more than once per round."
  - name: "Rend"
    desc: "⬻ claw"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37 - __2nd__ Invisibility (at will) - __4th__ Clairvoyance (×3), Translocate (at will) - __5th__ Scouting Eye (×3), Translocate - __8th__ Divine Decree - __Constant (7th)__ Truesight"
  - name: "Rituals"
    desc: "DC 37 - __1st__ Demonic Pact"
sourcebook: "_Monster Core_, page 81."
```

```encounter-table
name: Shemhazian
creatures:
  - 1: Shemhazian
```
