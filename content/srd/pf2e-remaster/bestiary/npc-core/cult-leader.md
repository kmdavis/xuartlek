---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cult Leader"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Cult Leader"
level: 7
source: "NPC Core"
aon_id: "creature-3539"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3539"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Cult Leader"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Arcana +13, Lore +19, Deception +16, Diplomacy +14, Intimidation +16, Occultism +17, Society +13"
abilityMods: [0, 4, 1, 4, 3, 5]
abilities_top:
  - name: "Items"
    desc: "ceremonial robes, indecipherable book of sigils (spellbook), _+1 shortsword_"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +15; __Will__: +18"
hp: 95
health:
  - name: "HP"
    desc: "95 __Protect the Master!__ ⬲ (auditory, concentrate, emotion, linguistic, mental, move)"
abilities_mid:
  - name: "Trigger"
    desc: "The cult leader is targeted with an attack, and a lower-ranking cultist is adjacent to them"
  - name: "Effect"
    desc: "The cult leader orders their cultist to leap in front of the attack. The cultist and cult leader swap places, and the cultist becomes the target of the attack. If the cultist has Fanatical Frenzy or a similar ability, they can activate it as a reaction if they take damage from the triggering attack."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _shortsword_ +16 (Agile, Finesse, Magical, versatile S) __Damage__ 1d6+6 piercing plus 2d8 void"
  - name: "Melee"
    desc: "⬻ fist +15 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Gather Converts"
    desc: "⬽ (Auditory, Concentrate, Emotion, Linguistic, Mental) With a short emotional phrase, the cult leader tries to sway the public to do their bidding. The cult leader tries to convince up to four bystanders in a crowd to cause a commotion, turn against a person or group, leave the area, protect the cult leader, or calm down. The cult leader attempts a single Deception check against the highest Perception DC among the targets."
  - name: "Critical Success"
    desc: "The targets believe the lie and act as directed for 1 minute. Additionally, one bystander remains by the cult leader's side, influenced enough to join the cult. All other targets become wise to the cult leader after 1 minute, at which point their attitude toward the leader worsens by one step."
  - name: "Success"
    desc: "As a critical success, but no bystander joins the cult permanently."
  - name: "Critical Failure"
    desc: "The crowd is unmoved and unamused, and their attitude toward the cult leader worsens by one step."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 26, attack +18 - __Cantrips (4th)__ Daze, Detect Magic, Guidance, Shield, Void Warp - __1st__ Bless, Illusory Disguise, Lock, Phantasmal Minion (4 slots) - __2nd__ Augury, Calm, Laughing Fit, Stupefy (4 slots) - __3rd__ Enthrall, Grim Tendrils, Haste, Mind Reading (4 slots) - __4th__ Honeyed Words, Outcast's Curse, Suggestion (3 slots)"
sourcebook: "_NPC Core_, page 100."
```

```encounter-table
name: Cult Leader
creatures:
  - 1: Cult Leader
```
