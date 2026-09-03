---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Deep One"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Deep One"
level: 1
source: "Monster Core 2"
aon_id: "creature-4314"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4314"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Deep One"
level: "Creature 1"
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision, wavesense (precise) 30 feet"
languages: "Aklo, Common"
skills:
  - name: "Skills"
    desc: "Athletics +6, Intimidation +5, Religion +6, Stealth +4, Survival +4"
abilityMods: [3, 1, 4, 2, 1, 1]
abilities_top:
  - name: "Pressurized"
    desc: "A deep one is immune to damage and other negative effects from changes in water pressure."
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +9; __Ref__: +4; __Will__: +8"
hp: 24
health:
  - name: "HP"
    desc: "24; __Immunities__ endless; __Resistances__ cold 2, piercing 3"
abilities_mid:
  - name: "Endless"
    desc: "A deep one doesn't age and is immune to spells and other effects that inflict magical aging. Unless killed, a deep one lives forever."
speed: "25 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +7 __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ claw +7 (Agile) __Damage__ 1d4+3 slashing"
abilities_bot:
  - name: "Fervent Frenzy"
    desc: "⬽ The deep one makes two claw Strikes and one jaws Strike in any order. If the target creature is currently frightened by a deep one's Share Devotion ability, it's off-guard against these attacks. The deep one becomes clumsy 1 until the start of their next turn."
  - name: "Share Devotion"
    desc: "⬺ (Concentrate, emotion, fear, mental) The deep one fills their enemies' minds with terrible hallucinations of the Outer Gods. All enemy creatures within a 30-foot emanation must attempt a DC 17 Will save; regardless of the result, a creature is temporarily immune to Share Devotion for 24 hours."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is frightened 1."
  - name: "Failure"
    desc: "The creature is frightened 2."
  - name: "Critical Failure"
    desc: "As failure, plus dazzled for as long as it's frightened."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 14, attack +6 - __Cantrips (1st)__ Daze - __1st__ Hydraulic Push"
sourcebook: "_Monster Core 2_, page 88."
```

```encounter-table
name: Deep One
creatures:
  - 1: Deep One
```
