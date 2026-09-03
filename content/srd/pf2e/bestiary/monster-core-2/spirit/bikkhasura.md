---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bikkhasura"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/asura
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Bikkhasura"
level: 20
source: "Monster Core 2"
aon_id: "creature-4088"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4088"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Bikkhasura"
level: "Creature 20"
size: "Huge"
trait_01: "Asura"
trait_02: "Spirit"
trait_03: "Unholy"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; darkvision, scent (imprecise) 60 feet, _truesight_"
languages: "Common, Diabolic; telepathy 100 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +33, Athletics +38, Diplomacy +36, Intimidation +34, Performance +34, Religion +35, Stealth +33"
abilityMods: [10, 7, 10, 7, 7, 8]
ac: 44
armorclass:
  - name: "AC"
    desc: "44; __Fort__: +35; __Ref__: +32; __Will__: +32 +2 status to all"
hp: 380
health:
  - name: "HP"
    desc: "380 , regeneration 20 (deactivated by holy); __Immunities__ curses, disease, illusions, poison, polymorph; __Weaknesses__ holy 15"
abilities_mid:
  - name: "Inescapable Aura"
    desc: "(aura, divine) 30 feet. Creatures cannot teleport into or out of the bikkhasura's aura. Creatures attempting to teleport into the aura instead teleport to the nearest edge of the aura. Any attempts to teleport out of the aura are automatically disrupted."
  - name: "Reactive Strike"
    desc: "⬲ The bikkhasura gains 5 additional reactions at the beginning of each of their turns that they can use only for a Reactive Strike."
speed: "40 feet, climb 40 feet, fly 40 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _spirit blade_ +37 (Magical, reach 15 feet, Unholy, versatile P) __Damage__ 4d6+15 slashing and 4d6 spirit"
  - name: "Melee"
    desc: "⬻ jaws +37 (Magical, Unholy) __Damage__ 4d10+15 piercing plus 4d6 persistent poison and Improved Grab"
  - name: "Melee"
    desc: "⬻ claw +35 (Agile, Magical, Unholy) __Damage__ 4d8+15 slashing plus curse of wisdom and 1d6 spirit"
abilities_bot:
  - name: "Bladestorm"
    desc: "⬺"
  - name: "Requirements"
    desc: "The bikkhasura is holding six spirit blades"
  - name: "Effect"
    desc: "The bikkhasura makes up to six spirit blade Strikes, each against a different target. These attacks count toward the bikkhasura's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks."
  - name: "Curse of Wisdom"
    desc: "(Curse)"
  - name: "Saving Throw"
    desc: "DC 42 Will"
  - name: "Stage 1"
    desc: "12d6 mental damage and target cannot use reactions (1 round)"
  - name: "Stage 2"
    desc: "14d6 mental damage and the target is slowed 2 (1 round)"
  - name: "Stage 3"
    desc: "15d6 mental damage and target is paralyzed (1 round)"
  - name: "Direct Spirit Blades"
    desc: "⬺"
  - name: "Requirements"
    desc: "The bikkhasura has their spirit blades"
  - name: "Effect"
    desc: "The bikkhasura directs one of its spirit blades to attack a target up to a distance of 50 feet away. Once a bikkhasura directs a spirit blade to attack a foe, the blade continues to make a single attack against that foe each round on the bikkhasura's turn until directed otherwise by the bikkhasura and as long as the foe remains within 50 feet of the bikkhasura. These weapons attack using the same statistics as the bikkhasura's spirit blade Strike and use the bikkhasura's multiple attack penalty. Any blades that are not within 50 feet of the bikkhasura at the end of its turn vanish."
  - name: "Glorious Visage"
    desc: "⬻ The asura sanctifies themselves as either holy or unholy, gaining the trait corresponding to their choice and losing the opposing trait; their strikes, spells, and abilities also gain the trait corresponding to their choice. The asura also gains weakness 15 to the opposing sanctification and loses any weakness to its chosen sanctification. The choice is permanent until the asura uses this ability to change their sanctification."
  - name: "Horrific Glimpse"
    desc: "⭓"
  - name: "Frequency"
    desc: "once per round"
  - name: "Trigger"
    desc: "The bikkhasura uses Glorious Visage"
  - name: "Effect"
    desc: "The bikkhasura explodes with spiritual energy, dealing 9d6 spirit damage to all creatures within 30 feet. This ability has the holy trait if the bikkhasura has the holy trait and the unholy trait when the bikkhasura has the unholy trait."
  - name: "Spirit Blades"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "The bikkhasura summons six blades made out of spiritual energy. The blades either appear in the bikkhasura's hands or float next to the bikkhasura until the asura directs one or spends an Interact action to grab it. The spirit blades can be dispelled with a successful counteract check (counteract rank 10, counteract DC 42). A successful counteract dispels all blades, even if some have been directed away from the bikkhasura."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44 - __5th__ Planar Tether, Translocate (at will), Wave of Despair (at will) - __8th__ Cursed Metamorphosis, Dispel Magic (×3), Unfettered Movement (×3), Weapon Storm - __9th__ Harm, Heal, Implosion, Metamorphosis, Wails of the Damned - __10th__ Freeze Time - __Constant (10th)__ Truesight"
sourcebook: "_Monster Core 2_, page 44."
```

```encounter-table
name: Bikkhasura
creatures:
  - 1: Bikkhasura
```
