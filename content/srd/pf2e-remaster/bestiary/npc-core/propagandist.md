---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Propagandist"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Propagandist"
level: 3
source: "NPC Core"
aon_id: "creature-3610"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3610"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Propagandist"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; (12 to Sense Motive)"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Diplomacy +11, Legal Lore +8, Performance +10, Society +10"
abilityMods: [0, 2, 1, 1, 3, 4]
abilities_top:
  - name: "Nuanced Spin"
    desc: "The propagandist phrases everything loosely and vaguely enough that, though it's always misleading, none of it is false. The propagandist can use Diplomacy instead of Deception to Create a Diversion or Feint, and instead of Intimidation to Coerce. A creature attempting to Sense Motive against the propagandist gets a result one degree of success worse than they rolled."
  - name: "Items"
    desc: "Dagger (3), lute, Shortsword, Writing Set"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +6; __Ref__: +9; __Will__: +12"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +9 (Agile, Finesse, versatile S) __Damage__ 1d6+4 piercing"
  - name: "Melee"
    desc: "⬻ dagger +9 (Agile, Finesse, versatile S) __Damage__ 1d4+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +9 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 21, 2 Focus Points - __Cantrips (2nd)__ Courageous Anthem, Rallying Anthem - __2nd__ Hymn of Healing, Lingering Composition"
  - name: "No Hard Feelings"
    desc: "⬺ (Auditory, Concentrate, emotional, Linguistic, Mental) The propagandist offers amnesty and other benefits to all who choose to join them. All enemies who can hear the propagandist must attempt a DC 19 Will save. If any of the propagandist's allies is currently benefiting from one of the propagandist's bard composition spells, any enemy who is aware of that takes a –2 circumstance penalty to the save."
  - name: "Critical Success"
    desc: "The creature sees through the propagandist's pitch and is temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature's conviction stumbles. Until the end of its next turn, the creature must succeed at a DC 5 flat check to target the propagandist with a hostile action."
  - name: "Critical Failure"
    desc: "The creature finds the propagandist's offer too good to pass up, switching sides in the combat and instantly gaining any benefits the propagandist is currently granting their allies. At the end of each of its turns, the creature can attempt another DC 19 Will save to snap out of it and rejoin their allies."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 21, attack +13 - __Cantrips (2nd)__ Bullhorn, Detect Magic, Haunting Hymn, Message, Summon Instrument - __1st__ Concordant Choir, Fear, Sanctuary (3 slots) - __2nd__ Blistering Invective, Paranoia (2 slots)"
sourcebook: "_NPC Core_, page 154."
```

```encounter-table
name: Propagandist
creatures:
  - 1: Propagandist
```
