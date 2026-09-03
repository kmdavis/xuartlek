---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lampad Queen"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/nymph
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Lampad Queen"
level: 15
source: "Monster Core 2"
aon_id: "creature-4492"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4492"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Lampad Queen"
level: "Creature 15"
size: "Medium"
trait_01: "Earth"
trait_02: "Fey"
trait_03: "Nymph"
trait_04: "Uncommon"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision"
languages: "Aklo, Common, Fey, Petran, Sakvroth; _speak with stones_"
skills:
  - name: "Skills"
    desc: "Acrobatics +27, Athletics +28, Deception +31, Diplomacy +33, Intimidation +33, Nature +27, Occultism +27, Performance +29, Society +25, Stealth +27"
abilityMods: [3, 8, 7, 4, 4, 8]
abilities_top:
  - name: "Cavern Empathy"
    desc: "The lampad queen can use Diplomacy to Make an Impression on and make very simple Requests of subterranean animals, plants, and fungi, as well as stones."
  - name: "Tied to the Land"
    desc: "A lampad queen is intrinsically tied to a specific underground region, usually a cave system. As long as the queen is healthy, the environment is exceptionally resilient, allowing the lampad queen to automatically attempt to counteract spells and rituals that would harm the environment, such as _blight_, with a +30 counteract modifier and a counteract rank of 8. When the lampad queen becomes physically or psychologically unhealthy, however, their warded region eventually becomes twisted or unhealthy as well. In that case, restoring the lampad queen swiftly heals the entire region."
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +26; __Ref__: +29; __Will__: +25"
hp: 235
health:
  - name: "HP"
    desc: "235; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Nymph's Beauty"
    desc: "(aura, emotion, incapacitation, mental, primal, visual) 30 feet. Creatures that start their turn in the aura must succeed at a DC 33 Will save or be confused by the lampad queen's unearthly beauty for 1 minute. While confused by this effect, the creature's confused actions never include harming the lampad queen."
speed: "30 feet, climb 30 feet (on stone only)"
attacks:
  - name: "Melee"
    desc: "⬻ earthen fist +29 (Agile, finesse) __Damage__ 3d10+9 bludgeoning plus 1d6 mental"
  - name: "Ranged"
    desc: "⬻ light wisp +29 (Magical, range increment 60 feet) __Damage__ 2d8+9 mental plus 2d6 fire and 2d6 vitality"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Polymorph, primal) Lampad queens can transform between their original form, which looks much like a typical nymph of their kind, and any Small or Medium humanoid form, typically choosing a version of their natural form that more closely resembles a humanoid."
  - name: "Despairing Weep"
    desc: "⬻ (Auditory, emotion, mental, primal)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The lampad queen begins a heart-wrenching fit of weeping, inspiring sympathetic sobbing in nearby creatures. Every non-lampad creature within 120 feet who hears the lampad's weeping must succeed at a DC 36 Will save with the effects of _wave of despair_."
  - name: "Focus Beauty"
    desc: "⬻ (Emotion, incapacitation, mental, primal, visual) The lampad queen focuses their beauty upon a target within their aura. The creature must attempt a DC 33 Will save. On a failure, it's affected as if by the queen's nymph beauty aura; if it was already affected by the aura, the conflicting emotions from the lampad queen's beauty intensify, causing the target to no longer get a flat check to end the confusion when it takes damage. The lampad queen can use a single action, which has the concentrate trait, to focus the emotions of a confused creature toward a particular emotion, causing it to spend its next turn sobbing uncontrollably, fawning over the lampad queen, or otherwise performing no actions beyond experiencing its emotions. Regardless of the save, the target is temporarily immune to Focus Beauty until the start of the lampad queen's next turn."
  - name: "Inspiration"
    desc: "⬽ (Emotion, mental, primal) A lampad queen can inspire a single intelligent creature by giving that creature a token of their favor, typically a lock of their hair. As long as the creature carries the token and remains in good standing with the lampad queen, the creature gains a +1 status bonus to all Crafting checks, Performance checks, and Will saves. If a lampad queen grants their Inspiration to a bard and they're that bard's muse, the bard gains an additional benefit depending on their muse theme: for lore muse, the bard also gains a +1 status bonus to all Lore checks; for maestro muse, the status bonus to Performance checks increases to +2 for the purpose of determining the effects of compositions; for polymath muse, the bard gains a +4 status bonus to untrained skill checks; and for all other muses, the Will save bonus increases to +2 against fey. Reciprocity Lampad queens tend to change emotions on a whim and mirror what they find in others. Those who treat the queen's domain with respect, they protect and reward, while those who harm it meet swift wrath. This leads to the vastly differing accounts of the queens' actions."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 38 - __Cantrips (8th)__ Detect Magic, Electric Arc, Guidance, Prestidigitation, Stabilize - __1st__ Ant Haul, Fleet Step, Gust of Wind - __2nd__ Animal Messenger, Enlarge, Revealing Light - __3rd__ Earthbind (×2), Haste - __4th__ Fly, Resist Energy, Unfettered Movement - __5th__ Impaling Spike, Magic Passage, Wall of Stone - __6th__ Mountain Resilience, Petrify, Slow - __7th__ Energy Aegis, Regenerate, Volcanic Eruption - __8th__ Earthquake, Summon Plant or Fungus"
  - name: "Primal Innate Spells"
    desc: "DC 38 - __Cantrips (8th)__ Light - __2nd__ Revealing Light - __3rd__ One with Stone (at will) - __4th__ Shape Stone - __7th__ Heal - __8th__ Pummeling Rubble - __Constant (6th)__ Speak with Stones"
sourcebook: "_Monster Core 2_, page 237."
```

```encounter-table
name: Lampad Queen
creatures:
  - 1: Lampad Queen
```
