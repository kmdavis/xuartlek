---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ancient Phase Dragon"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/arcane
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Ancient Phase Dragon"
level: 18
source: "Monster Core 2"
aon_id: "creature-4356"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4356"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ancient Phase Dragon"
level: "Creature 18"
size: "Gargantuan"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: "Uncommon"
modifier: 32
perception:
  - name: "Perception"
    desc: "Perception +32; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: "Skills"
    desc: "Acrobatics +34, Arcana +35, Athletics +32, Diplomacy +33, Lore +37, Nature +31, Occultism +33, Religion +31"
abilityMods: [6, 8, 4, 9, 7, 6]
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +27; __Ref__: +32; __Will__: +31 +2 status to all saves vs. arcane"
hp: 250
health:
  - name: "HP"
    desc: "250; __Immunities__ immobilized, paralyzed, sleep"
abilities_mid:
  - name: "Unerring Location"
    desc: "The dragon automatically attempts to counteract any teleportation effect that targets them (counteract rank 9th, counteract modifier +32). The dragon can choose to be affected normally instead. Other creatures targeted by the same effect remain affected normally. __Shoo!__ ⬲ (arcane, teleportation)"
  - name: "Trigger"
    desc: "An enemy within 15 feet damages the dragon"
  - name: "Effect"
    desc: "The dragon teleports the creature up to 35 feet away. The destination must be on the ground and in a space with no hazards."
speed: "60 feet, fly 180 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +34 (Magical, reach 15 feet) __Damage__ 3d12+16 piercing"
  - name: "Melee"
    desc: "⬻ claw +34 (Agile, magical, reach 10 feet) __Damage__ 3d8+16 slashing"
  - name: "Melee"
    desc: "⬻ tail +32 (Magical, reach 20 feet) __Damage__ 3d10+16 bludgeoning"
abilities_bot:
  - name: "Blinking Barrage"
    desc: "⬽ (Arcane, concentrate, teleportation) The dragon channels all their teleportation prowess into a remarkable series of blows. The dragon teleports up to 60 feet to a space adjacent to a creature and makes a claw Strike against that creature. The dragon can do this up to four times, teleporting to a different creature each time. Each attack counts toward their multiple attack penalty, but the penalty does not increase until all attacks have been made. The dragon cannot take actions with the teleportation trait again until the end of their next turn."
  - name: "Dislocating Breath"
    desc: "⬺ (Arcane, teleportation) The dragon exhales a swirl of energy that pulls creatures apart, dealing 17d6 force damage in a 50-foot cone (DC 40 basic Reflex save). The dragon can teleport any creature that fails its save, teleporting that creature up to 50 feet (or twice as far on a critical failure) in any direction. The destination must be on the ground and in a space with no hazards. The dragon can't use Dislocating Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Dislocating Breath or regain an expended teleportation spell."
  - name: "Phase Jump"
    desc: "⬻ (Arcane, concentrate, teleportation)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The dragon teleports up to 90 feet. If they are airborne, they maintain their momentum, and do not fall at the end of their turn, even if they didn't use an action to Fly."
  - name: "Portal Strike"
    desc: "⬺ (Arcane, concentrate, manipulate, teleportation) The dragon momentarily opens a small portal and makes a claw Strike against a creature within 90 feet. The target is off-guard to the Strike."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 40 - __Cantrips (9th)__ Detect Magic, Read Aura - __4th__ Flicker, Planar Tether, Translocate (at will) - __5th__ Translocate - __6th__ Teleport - __7th__ Interplanar Teleport, Planar Seal - __8th__ Quandary - __Constant (7th)__ Know the Way"
sourcebook: "_Monster Core 2_, page 126."
```

```encounter-table
name: Ancient Phase Dragon
creatures:
  - 1: Ancient Phase Dragon
```
