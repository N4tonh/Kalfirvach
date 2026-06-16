#!/usr/bin/env python3
"""
Script para corregir problemas de integridad en el léxico de Kalfírvach v1.3
Problemas a corregir:
1. Entradas sin POS en biologia_y_micologia y profesiones_y_roles
2. Entradas sin campo kalfirvach
3. Entradas con IPA sin acento primario (ˈ)
4. Actualizar metadata
5. Añadir nuevos verbos de cocina (corregidos fonológicamente)
"""

import json
import re

def fix_missing_pos(entry):
    """Añadir pos: 'noun' si falta en categorías específicas"""
    if 'pos' not in entry or entry['pos'] is None or entry['pos'] == '':
        entry['pos'] = 'noun'
        return True
    return False

def fix_missing_kalfirvach(entry):
    """Añadir campo kalfirvach si falta, copiando de forma_final"""
    if 'kalfirvach' not in entry or entry['kalfirvach'] is None or entry['kalfirvach'] == '':
        if 'forma_final' in entry and entry['forma_final']:
            entry['kalfirvach'] = entry['forma_final']
            return True
    return False

def fix_missing_ipa_accent(entry):
    """Añadir acento primario (ˈ) en IPA si falta"""
    if 'ipa' in entry and entry['ipa']:
        ipa = entry['ipa']
        # Si ya tiene acento, no hacer nada
        if 'ˈ' in ipa:
            return False
        
        # Extraer solo la parte fonética entre slashes
        match = re.match(r'^/(.*)/$', ipa)
        if match:
            phonetic = match.group(1)
            
            # Regla: monosílabos también llevan acento
            # Contar sílabas (aproximado por vocales)
            vowels = re.findall(r'[aeiouæøʉyɛɔɑːīūēōā]', phonetic, re.IGNORECASE)
            
            if len(vowels) >= 1:
                # Encontrar primera vocal o diptongo
                # Insertar acento antes de la primera sílaba
                # Patrón: buscar inicio de sílaba tónica (generalmente primera)
                
                # Casos especiales: si empieza con consonante + líquida/nasal, el acento va después
                if re.match(r'^[pbtdkgfvsʃxɣθlmnrwjqj][lrwnmj]', phonetic):
                    # Buscar primera vocal después del cluster
                    vowel_match = re.search(r'[aeiouæøʉyɛɔɑːīūēōā]', phonetic, re.IGNORECASE)
                    if vowel_match:
                        pos = vowel_match.start()
                        new_phonetic = phonetic[:pos] + 'ˈ' + phonetic[pos:]
                        entry['ipa'] = '/' + new_phonetic + '/'
                        return True
                else:
                    # Acento en primera sílaba
                    new_phonetic = 'ˈ' + phonetic
                    entry['ipa'] = '/' + new_phonetic + '/'
                    return True
        
        return False
    return False

def add_cooking_verbs(categorias):
    """Añadir nuevos verbos de cocina corregidos fonológicamente"""
    
    cooking_verbs = [
        {
            "concepto": "hervir",
            "forma_final": "kvathel",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "क्वथति kvathati 'hervir' / ζέω zéō 'hervir'",
                "corpus": "Skt. medical texts / Hippocrates"
            },
            "transformacion": [
                "kvathati→kvath (apócope), + -el (sufijo verbal)",
                "convergencia semántica 'calentar hasta ebullición'"
            ],
            "derivaciones": [],
            "kalfirvach": "kvathel",
            "pos": "verb",
            "ipa": "/ˈkva.tʰel/"
        },
        {
            "concepto": "hornear",
            "forma_final": "pakar",
            "origen": {
                "lengua": "Sánscrito/Persa",
                "raiz_original": "पचति pacati 'cocinar' / پختن pukhtan 'cocinar, hornear'",
                "corpus": "Skt. culinary / Pers. classical"
            },
            "transformacion": [
                "pacati→pac→pak (fortición final)",
                "pukhtan→puk→pak (reducción, convergencia)"
            ],
            "derivaciones": [],
            "kalfirvach": "pakar",
            "pos": "verb",
            "ipa": "/ˈpa.kar/"
        },
        {
            "concepto": "mezclar",
            "forma_final": "misal",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "मिश्रयति miśrayati 'mezclar' / μίγνυμι mignymi 'mezclar'",
                "corpus": "Skt. alchemical / Greek technical"
            },
            "transformacion": [
                "miśrayati→miśra→misra→misa (simplificación)",
                "mignymi→mig→mis (asimilación)"
            ],
            "derivaciones": [],
            "kalfirvach": "misal",
            "pos": "verb",
            "ipa": "/ˈmi.sal/"
        },
        {
            "concepto": "cortar",
            "forma_final": "kiras",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "कृन्तति kṛntati 'cortar' / κείρω keírō 'cortar, rapar'",
                "corpus": "Skt. epic / Homeric Greek"
            },
            "transformacion": [
                "kṛntati→kṛt→kir (vocalización ṛ→i)",
                "keírō→keir→kir (reducción)"
            ],
            "derivaciones": [],
            "kalfirvach": "kiras",
            "pos": "verb",
            "ipa": "/ˈki.ras/"
        },
        {
            "concepto": "pelar",
            "forma_final": "tuvakar",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "त्वच् tvac 'piel, cáscara' / δέρμα dérma 'piel'",
                "corpus": "Skt. anatomical / Greek medical"
            },
            "transformacion": [
                "tvac→tva (epéntesis u→tu)",
                "dérma→der→kar (metátesis, convergencia)"
            ],
            "derivaciones": [],
            "kalfirvach": "tuvakar",
            "pos": "verb",
            "ipa": "/tu.ˈva.kar/"
        },
        {
            "concepto": "rallar",
            "forma_final": "kharit",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "खरति kharati 'rascar, rallar' / ξέω xéō 'raspar, rallar'",
                "corpus": "Skt. technical / Greek domestic"
            },
            "transformacion": [
                "kharati→khar (apócope)",
                "xéō→xe→khe→kha (aspiración)"
            ],
            "derivaciones": [],
            "kalfirvach": "kharit",
            "pos": "verb",
            "ipa": "/ˈkʰa.rit/"
        },
        {
            "concepto": "batir",
            "forma_final": "mathel",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "मथ्नाति mathnāti 'batir, agitar' / ταράσσω tarássō 'agitar, perturbar'",
                "corpus": "Skt. culinary / Greek technical"
            },
            "transformacion": [
                "mathnāti→math (apócope)",
                "tarássō→tar→thal→thel (asimilación)"
            ],
            "derivaciones": [],
            "kalfirvach": "mathel",
            "pos": "verb",
            "ipa": "/ˈma.tʰel/"
        },
        {
            "concepto": "amasar",
            "forma_final": "mardar",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "मृद्नाति mṛdnāti 'amasar, aplastar' / μάσσω mássō 'amasar'",
                "corpus": "Skt. culinary / Greek domestic"
            },
            "transformacion": [
                "mṛdnāti→mṛd→mard (vocalización ṛ→ar)",
                "mássō→mas→mar (nasalización)"
            ],
            "derivaciones": [],
            "kalfirvach": "mardar",
            "pos": "verb",
            "ipa": "/ˈmar.dar/"
        },
        {
            "concepto": "fermentar",
            "forma_final": "suray",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "सुरा surā 'licor fermentado' / ζύτη zýtē 'cerveza, fermento'",
                "corpus": "Skt. ritual / Greek technical"
            },
            "transformacion": [
                "surā→sur (apócope)",
                "zýtē→zyt→sut→sur (asimilación)"
            ],
            "derivaciones": [],
            "kalfirvach": "suray",
            "pos": "verb",
            "ipa": "/su.ˈraj/"
        },
        {
            "concepto": "marinar",
            "forma_final": "lunik",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "लवण lavaṇa 'sal' / ἅλς háls 'sal'",
                "corpus": "Skt. culinary / Greek domestic"
            },
            "transformacion": [
                "lavaṇa→lav→lun (nasalización)",
                "háls→hal→luk (metátesis)"
            ],
            "derivaciones": [],
            "kalfirvach": "lunik",
            "pos": "verb",
            "ipa": "/ˈlu.nik/"
        },
        {
            "concepto": "glasear",
            "forma_final": "grisay",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "घृत ghṛta 'ghee, grasa' / χρῖσμα chrîsma 'ungüento'",
                "corpus": "Skt. ritual / Greek religious"
            },
            "transformacion": [
                "ghṛta→ghṛ→gri (vocalización ṛ→i)",
                "chrîsma→chris→gris (desaspiración)"
            ],
            "derivaciones": [],
            "kalfirvach": "grisay",
            "pos": "verb",
            "ipa": "/ˈɣri.saj/"
        },
        {
            "concepto": "escaldar",
            "forma_final": "dahul",
            "origen": {
                "lengua": "Sánscrito/Persa",
                "raiz_original": "दहति dahati 'quemar, escaldar' / داغ dāgh 'marca de quemadura'",
                "corpus": "Skt. medical / Pers. classical"
            },
            "transformacion": [
                "dahati→dah (apócope)",
                "dāgh→dag→dah (asimilación)"
            ],
            "derivaciones": [],
            "kalfirvach": "dahul",
            "pos": "verb",
            "ipa": "/ˈda.hul/"
        },
        {
            "concepto": "pochar",
            "forma_final": "manday",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "मन्द manda 'lento, suave' / βραδύς bradýs 'lento'",
                "corpus": "Skt. culinary / Greek technical"
            },
            "transformacion": [
                "manda→mand (apócope)",
                "bradýs→brad→mad (simplificación)"
            ],
            "derivaciones": [],
            "kalfirvach": "manday",
            "pos": "verb",
            "ipa": "/man.ˈdaj/"
        },
        {
            "concepto": "saltear",
            "forma_final": "plavas",
            "origen": {
                "lengua": "Sánscrito/Griego",
                "raiz_original": "प्लवते plavate 'flotar, saltar' / ἅλλομαι hallomai 'saltar'",
                "corpus": "Skt. poetic / Greek epic"
            },
            "transformacion": [
                "plavate→plav (apócope)",
                "hallomai→hal→plas (asimilación)"
            ],
            "derivaciones": [],
            "kalfirvach": "plavas",
            "pos": "verb",
            "ipa": "/ˈpla.vas/"
        },
        {
            "concepto": "gratinar",
            "forma_final": "zarik",
            "origen": {
                "lengua": "Persa/Sánscrito",
                "raiz_original": "زر zar 'oro' / स्वर्ण svarṇa 'oro, dorado'",
                "corpus": "Pers. classical / Skt. ritual"
            },
            "transformacion": [
                "zar→zar (directo)",
                "svarṇa→svar→sar→zar (simplificación)"
            ],
            "derivaciones": [],
            "kalfirvach": "zarik",
            "pos": "verb",
            "ipa": "/ˈza.rik/"
        }
    ]
    
    if 'comida_y_cocina' not in categorias:
        print("ERROR: categoría 'comida_y_cocina' no encontrada")
        return 0
    
    existing_concepts = set()
    for entry in categorias['comida_y_cocina']['entradas']:
        if 'concepto' in entry:
            existing_concepts.add(entry['concepto'].lower())
    
    added_count = 0
    for verb in cooking_verbs:
        concepto_lower = verb['concepto'].lower()
        if concepto_lower not in existing_concepts:
            categorias['comida_y_cocina']['entradas'].append(verb)
            added_count += 1
        else:
            print(f"  ⚠️  Verbo '{verb['concepto']}' ya existe, saltando...")
    
    return added_count

def main():
    print("🔧 Iniciando corrección de integridad del léxico Kalfírvach v1.3...\n")
    
    # Cargar léxico
    with open('/workspace/kalfirvach_lexicon_v1.3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    categorias = data['kalfirvach_lexicon_v1.3']['categorias']
    metadata = data['kalfirvach_lexicon_v1.3']['metadata']
    
    total_entries = 0
    fixed_pos = 0
    fixed_kalfirvach = 0
    fixed_ipa = 0
    
    # Contar entradas totales y corregir
    for cat_name, categoria in categorias.items():
        if 'entradas' not in categoria:
            continue
            
        for entry in categoria['entradas']:
            total_entries += 1
            
            # Corrección 1: POS faltante
            if cat_name in ['biologia_y_micologia', 'profesiones_y_roles']:
                if fix_missing_pos(entry):
                    fixed_pos += 1
            
            # Corrección 2: kalfirvach faltante
            if fix_missing_kalfirvach(entry):
                fixed_kalfirvach += 1
            
            # Corrección 3: IPA sin acento
            if fix_missing_ipa_accent(entry):
                fixed_ipa += 1
    
    print(f"📊 Total de entradas procesadas: {total_entries}")
    print(f"✅ POS corregidos: {fixed_pos}")
    print(f"✅ Campos 'kalfirvach' añadidos: {fixed_kalfirvach}")
    print(f"✅ Acentos IPA añadidos: {fixed_ipa}")
    
    # Corrección 4: Actualizar metadata
    print("\n🔄 Actualizando metadata...")
    metadata['version'] = '1.3'
    metadata['total_entries'] = total_entries
    # Eliminar campos redundantes si existen
    if 'total_entradas' in metadata:
        del metadata['total_entradas']
    if 'total_categorias' in metadata:
        del metadata['total_categorias']
    metadata['total_categories'] = len(categorias)
    
    # Corrección 5: Añadir verbos de cocina
    print("\n🍳 Añadiendo verbos de cocina...")
    added_cooking = add_cooking_verbs(categorias)
    print(f"✅ Verbos de cocina añadidos: {added_cooking}")
    
    # Recalcular total después de añadir
    new_total = sum(len(cat['entradas']) for cat in categorias.values() if 'entradas' in cat)
    metadata['total_entries'] = new_total
    
    # Guardar léxico corregido
    output_path = '/workspace/kalfirvach_lexicon_v1.3_fixed.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Léxico corregido guardado en: {output_path}")
    print(f"📈 Nuevo total de entradas: {new_total}")
    print(f"📁 Total de categorías: {len(categorias)}")
    print("\n✨ ¡Corrección completada exitosamente!")

if __name__ == '__main__':
    main()
