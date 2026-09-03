---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Resurrection Dragon"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Young Resurrection Dragon"
level: 8
source: "Monster Core 2"
aon_id: "creature-4360"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4360"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Resurrection Dragon"
level: "Creature 8"
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Necril"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Arcana +15, Athletics +18, Diplomacy +18, Medicine +18, Necromancy Lore +19, Religion +18, Stealth +17"
abilityMods: [6, 3, 4, 3, 6, 4]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +15; __Ref__: +14; __Will__: +19"
hp: 140
health:
  - name: "HP"
    desc: "140; __Immunities__ death effects, paralyzed, sleep; __Resistances__ spirit 10"
abilities_mid:
  - name: "Risen Commander"
    desc: "(divine) A resurrection dragon has a strong connection with its minions and can Sustain _summon undead_ or _invoke spirits_ as a free action once per turn. __Reawaken!__ ⬲ (divine, spirit, vitality)"
  - name: "Trigger"
    desc: "A living creature the resurrection dragon can see dies"
  - name: "Effect"
    desc: "The resurrection dragon uses divine and vital energy to retether the soul to its dead body. The willing creature is returned to life with the dying 1 condition at the start of its next turn. A creature can be resurrected by this ability only once."
  - name: "Siphon Life"
    desc: "⬲ (divine, healing, vitality)"
  - name: "Trigger"
    desc: "A creature within 60 feet uses a healing effect that restores Hit Points"
  - name: "Effect"
    desc: "The resurrection dragon redirects vital energies away from the effect, minimizing its impact. The triggering effect results in the minimum amount on any dice rolls to restore Hit Points, and any flat values for restoring Hit Points (such as the additional Hit Points for a two-action _heal_ spell) are cut in half. The dragon then gains 1d8 temporary Hit Points that last for 1 round."
speed: "30 feet, fly 120 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +20 (Magical, reach 10 feet) __Damage__ 2d10+9 piercing plus 1d6 void"
  - name: "Melee"
    desc: "⬻ claw +20 (Agile, magical) __Damage__ 2d8+9 slashing"
  - name: "Melee"
    desc: "⬻ tail +18 (Magical, reach 15 feet) __Damage__ 2d10+9 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw strikes and one tail strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Soul Siphoning Breath whenever they score a critical hit with a Strike."
  - name: "Soul Siphoning Breath"
    desc: "⬺ (Divine, void) The dragon unleashes a torrent of divine energy, dealing 7d6 void damage in a 30-foot cone (DC 26 basic Fortitude save) that draws the life force from creatures within. The dragon gains fast healing 5 until their Soul Siphoning Breath recharges. The resurrection dragon can't use Soul Siphoning Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26 - __Cantrips (4th)__ Guidance, Stabilize, Void Warp - __4th__ Harm (×2), Summon Undead (at will), Talking Corpse"
sourcebook: "_Monster Core 2_, page 129."
```

```encounter-table
name: Young Resurrection Dragon
creatures:
  - 1: Young Resurrection Dragon
```
