---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Satyr"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/medium
statblock: inline
name: "Satyr"
level: 4
source: "Monster Core"
aon_id: "creature-3173"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3173"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Satyr"
level: "Creature 4"
size: "Medium"
trait_01: "Fey"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; low-light vision"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Athletics +8, Deception +13, Diplomacy +13, Intimidation +11, Nature +9, Performance +13, Stealth +11, Survival +8"
abilityMods: [3, 4, 1, 1, 2, 5]
abilities_top:
  - name: "Sylvan Wine"
    desc: "(emotion, mental, primal) A satyr's wineskin magically enchants any alcohol inside. With an Interact action, a living creature can imbibe the alcohol and gain a +1 item bonus to Will saves and a +3 item bonus to Will saves against fear effects for the following hour. When the wineskin is removed from a satyr's person, the magic remains only until the wine spoils. The wineskin holds up to eight drafts of wine."
  - name: "Items"
    desc: "Dagger, panpipes, Shortbow (20 arrows), wineskin"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +9; __Ref__: +11; __Will__: +12"
hp: 80
health:
  - name: "HP"
    desc: "80; __Weaknesses__ cold iron 5"
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +14 (Agile, Finesse, versatile S) __Damage__ 1d4+6 piercing"
  - name: "Ranged"
    desc: "⬻ shortbow +14 (deadly d10, range increment 60 feet, reload 0) __Damage__ 1d6 +3 piercing"
  - name: "Ranged"
    desc: "⬻ dagger +14 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+6 piercing"
abilities_bot:
  - name: "Fleet Performer"
    desc: "When the satyr Plays the Pipes to cast a spell, he can Step or Stride as part of the activity."
  - name: "Play the Pipes"
    desc: "⬽ (Auditory, Primal)"
  - name: "Requirements"
    desc: "The satyr is holding a musical instrument"
  - name: "Effect"
    desc: "The satyr plays a melody on his instrument to cast charm, _fear_, _sleep_, or _suggestion_ without expending the spell slot. The spell gains the auditory trait and targets all creatures in a 60-foot emanation instead of its usual targets. A creature that succeeds at its Will save against any spell is then temporarily immune from spells played from that satyr's pipes for 1 minute. Satyrs are immune to this music. Satyr Pipes A satyr's gear is valuable, particularly his fine panpipes. Depending on the type of music they prefer to play, satyrs may be able to cast different 4th-rank spells, such as _laughing fit_ or _paranoia_. Satyrs also stow caches of alcohol, rich food, and pieces of fine art (especially erotic art) in hollows and glades they frequent."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ Courageous Anthem, Figment, Light, Triple Time, Uplifting Overture - __4th__ Charm, Fear, Sleep, Suggestion"
sourcebook: "_Monster Core_, page 296."
```

```encounter-table
name: Satyr
creatures:
  - 1: Satyr
```
