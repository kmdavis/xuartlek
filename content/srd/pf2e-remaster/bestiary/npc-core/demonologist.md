---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Demonologist"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Demonologist"
level: 7
source: "NPC Core"
aon_id: "creature-3540"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3540"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Demonologist"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15"
languages: "Chthonian, Common"
skills:
  - name: "Skills"
    desc: "Academia Lore +14, Arcana +16, Demon Lore +18, Diplomacy +11, Religion +15"
abilityMods: [3, 1, 2, 4, 4, 0]
abilities_top:
  - name: "Demonic Temptation"
    desc: "(divine, mental) Demonic study has garnered the attention of at least one demon who is actively trying to possess the demonologist. When the demonologist publicly espouses the benefits of demonic power (whether they believe it a good thing or not), they gain a +1 status bonus to skill checks, AC, and saves for 1 day. These bonuses don't apply against demons. At the end of the day, the demonologist must attempt a DC 20 Will save, becoming possessed for 1 day on a failure (or permanently on a critical failure)."
  - name: "Items"
    desc: "_+1 longspear_, robes, _Fiendish Hypotheses and Protections from Same_ (spellbook)"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +13; __Ref__: +12; __Will__: +15"
hp: 100
health:
  - name: "HP"
    desc: "100"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longspear_ +17 (Magical, Reach) __Damage__ 1d8+9 piercing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+9 bludgeoning"
abilities_bot:
  - name: "Breach the Outer Rifts"
    desc: "⭓"
  - name: "Requirements"
    desc: "The demonologist's last action was to cast a non-cantrip spell"
  - name: "Effect"
    desc: "The demonologist siphons energy drawn from the Outer Rifts into their weapon. Until the end of the turn, the weapon deals an extra 2d6 damage. Roll 1d20 to determine the type: 1–7 acid, 8–9 cold, 10–11 electricity, 12–18 fire, 19–20 void."
  - name: "Demon Summoning"
    desc: "The demonologist can cast a 5th-rank _summon fiend_ arcane spell to summon a demon. To do so, they must sacrifice two 4th-rank prepared spells and voluntarily take 4d12 mental damage that can't be reduced or prevented. If the demonologist is unable to Sustain the Spell, including if they're knocked out or killed, the spell continues, but the GM rolls a DC 10 flat check each round, ending the spell on a failure."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 25, attack +17 - __Cantrips (4th)__ Caustic Blast, Daze, Detect Magic, Light, Read Aura - __1st__ Fear (×2), Fleet Step, Mending - __2nd__ Blur, Environmental Endurance, Laughing Fit, See the Unseen - __3rd__ Acid Grip, Fireball, Grease, Slow - __4th__ Clairvoyance, Dispelling Globe, Wall of Fire"
sourcebook: "_NPC Core_, page 100."
```

```encounter-table
name: Demonologist
creatures:
  - 1: Demonologist
```
