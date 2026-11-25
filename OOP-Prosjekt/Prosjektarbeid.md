# OOP-Prosjektarbeid

## Hva gjør programmet?

Programmet er et enkelt turbasert "fighting" game hvor man kan opprette karakterer, og bruke dem til å kjempe mot en datamaskin motstander. Viktige elementer for programmet innebærer blant annet en while loop som representerer selve "game-loopen" og en overordnet "Pokemon" klasse som definerer grunnleggende attributer for både datamaskinen og brukerens karakterer. Jeg har også en egen sub-klasse for datamaskinens karakterer, slik at den kan arve flere av attributene og metodene fra super-klassen (Pokemon).

## Hvordan kjøres programmet?

Programmet kjøres gjennom terminalen, men bruker biblioteker som random og rich for å fungere/forbedre det visuelle. Man kjører BattleSimulator.py som "main" filen, mens Visuals.py blir importert til hovedfilen og brukes direkte der.

## Kilder

Jeg har brukt nettsteder som W3schools og Stack Overflow til å innimellom søke opp ting som jeg var litt usikker på, eller ville undersøke litt nærmere. Blant annet leste jeg meg litt opp på list funksjonen i python, som lar deg samle informasjon i en liste.

## Bruk av KI

Jeg har brukt KI til å komme med forslag til overordnede prosjektideer, slik at jeg fikk noen forslag til ulike ideer til et prosjekt. Jeg har også brukt KI til å hjelpe litt med planleggingen av hva som kreves for å lage/utføre ideen jeg bestemte meg for, slik at jeg hadde en noenlunde ide over hva jeg måtte gjøre. Og hva som kunne vært lurt å implementere først. Hvis jeg satt fast, prøvde jeg først å undersøke litt selv, men spurte gjerne KI om hint til hva som var feil, og hvorfor denne feilen var et problem. Jeg prøvde altså å bruke KI på en måte som gjorde at jeg lærte mest mulig, og forsto hva som var feil/hvorfor det var feil.

## Logg

Jeg startet først med å finne ut av hvilket type prosjekt jeg ville arbeide med. Når jeg hadde landet det ned, skaffet jeg en oversikt over hvilke komponenter som kunne være lurt å implementere, samt en noenlunde rekkefølge for hva som skal gjøres når. Når jeg begynte med selve programmeringen, startet jeg først med å innføre en overordnet klasse "Pokemon", og funksjonalitet som lar brukeren lage karakterer. Deretter jobbet jeg med å la brukeren velge hvilken karakter som skal kjempe, og hvilket trekk brukerens karakter skulle bruke. Jeg implementerte også at datamaskinen velger hvilken motstander som skal sendes ut først, samt hvilket trekk mostander karakteren skal bruke. Jeg jobbet videre med å implementere ting som at man kan velge mellom å bytte eller kjempe, samt at man bytter ut når man dør hvis man har en karakter i livet. Når jeg for det meste var ferdig med det grunnleggende for spillet, jobbet jeg med å implementere rich for å forbedre det visuelle i terminalen, samt gjøre små endringer i koden her og der for å forbedre den.