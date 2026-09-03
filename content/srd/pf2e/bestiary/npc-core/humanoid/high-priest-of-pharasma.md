---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "High Priest of Pharasma"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "High Priest of Pharasma"
level: 9
source: "NPC Core"
aon_id: "creature-3447"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3447"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "High Priest of Pharasma"
level: "Creature 9"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20"
languages: "Common, Requian"
skills:
  - name: "Skills"
    desc: "Boneyard Lore +27, Diplomacy +25, Intimidation +17, Medicine +18, Performance +17, Religion +26"
abilityMods: [1, 2, -1, 3, 5, 4]
abilities_top:
  - name: "Religious Specialist"
    desc: "For encounters involving religious debates, church politics, and conflicts of doctrine, the high priest is a 13th-level challenge."
  - name: "Items"
    desc: "_+1 striking dagger_, Hand Crossbow (20 bolts), Healer's Toolkit, _holy water_ (4), religious symbol of Pharasma, religious text of Pharasma, _scroll of cleanse affliction_ (4th rank)"
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +16; __Ref__: +17; __Will__: +21"
hp: 150
health:
  - name: "HP"
    desc: "150; __Resistances__ void 5"
abilities_mid:
  - name: "Steward of the Faithful"
    desc: "(aura, divine, vitality) 30 feet. Each ally in the aura who worships Pharasma gains resistance 5 to void and a +1 status bonus to Will saves, Diplomacy checks, and Medicine checks."
  - name: "Unshakable Faith"
    desc: "During a religious debate, clash of church politics, or similar conflict, the high priest gains a +4 circumstance bonus to Perception check to Sense Motive and to their Perception DC against attempt to lie to them."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _dagger_ +18 (Agile, Finesse, Magical, versatile S) __Damage__ 2d4+7 piercing plus 1d10 spirit"
  - name: "Melee"
    desc: "⬻ fist +17 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+7 bludgeoning plus 1d10 spirit"
  - name: "Ranged"
    desc: "⬻ hand crossbow +17 (range increment 60 feet, reload 1) __Damage__ 1d6+7 piercing plus 1d10 spirit"
  - name: "Ranged"
    desc: "⬻ _dagger_ +17 (Agile, Magical, thrown 10 feet, versatile S) __Damage__ 2d4+7 piercing plus 1d10 spirit"
abilities_bot:
  - name: "Cleric Domain Spells"
    desc: "DC 28, 2 Focus Points - __5th__ Death's Call, Eradicate Undeath"
  - name: "Healing Hands"
    desc: "When the high priest casts _heal_, they roll d10s instead of d8s."
  - name: "Restorative Channel"
    desc: "The high priest can sacrifice one prepared heal spell to instead cast _cleanse affliction_, _clear mind_, _sound body_, or _sure footing_ at the same spell rank."
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 28, attack +20 - __Cantrips (4th)__ Daze, Detect Magic, Message, Read Aura, Vitality Lash - __1st__ Command, Mindlink, Spirit Link - __2nd__ Augury, Darkvision, Status - __3rd__ Fear, Ghostly Weapon, Heroism - __4th__ Holy Light (×2), Vital Beacon - __5th__ Breath of Life, Heal (×5), Vision of Death"
  - name: "Rituals"
    desc: "DC 28 - __2nd__ Consecrate, Heartbond - __4th__ Atone, Rest Eternal - __5th__ Resurrect"
sourcebook: "_NPC Core_, page 33."
```

```encounter-table
name: High Priest of Pharasma
creatures:
  - 1: High Priest of Pharasma
```
