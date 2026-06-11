#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de actualización segura del léxico Kalfírvach v1.2
- Corrige POS faltantes en biología y profesiones
- Añade campo kalfirvach faltante
- Corrige IPA sin acento primario
- Añade 15 verbos de cocina
"""

import json
import re

def main():
    # Cargar el léxico actual completo
    with open('kalfirvach_lexicon_v1.2.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Acceder a la estructura correcta
    lexicon_root = data['kalfirvach_lexicon_v1.2']
    categorias = lexicon_root['categorias']
    metadata = lexicon_root['metadata']
    
    contador_correcciones = 0
    contador_nuevas = 0
    
    print("🔍 Iniciando correcciones de integridad...")
    
    # --- CORRECCIÓN 1: POS faltante en biología y profesiones ---
    for cat_name in ['biologia_y_micologia', 'profesiones_y_roles']:
        if cat_name in categorias:
            for entrada in categorias[cat_name]['entradas']:
                if 'pos' not in entrada or entrada.get('pos') is None:
                    entrada['pos'] = 'noun'
                    contador_correcciones += 1
            print(f"   ✅ {cat_name}: POS corregidas")
        else:
            print(f"   ⚠️ Categoría {cat_name} no encontrada")
    
    # --- CORRECCIÓN 2: Campo kalfirvach faltante ---
    for cat_name, cat_data in categorias.items():
        for entrada in cat_data['entradas']:
            if 'kalfirvach' not in entrada or not entrada.get('kalfirvach'):
                if 'forma_final' in entrada and entrada['forma_final']:
                    entrada['kalfirvach'] = entrada['forma_final']
                    contador_correcciones += 1
    print(f"   ✅ Campo kalfirvach añadido a entradas faltantes")
    
    # --- CORRECCIÓN 3: IPA sin acento (solo si falta completamente) ---
    for cat_name, cat_data in categorias.items():
        for entrada in cat_data['entradas']:
            if 'ipa' in entrada and entrada['ipa']:
                ipa = entrada['ipa']
                # Si no tiene acento primario ˈ
                if 'ˈ' not in ipa:
                    # Patrón seguro: /contenido/
                    if ipa.startswith('/') and ipa.endswith('/'):
                        content = ipa[1:-1]
                        # Añadir acento al inicio (primera sílaba)
                        entrada['ipa'] = '/' + 'ˈ' + content + '/'
                        contador_correcciones += 1
    print(f"   ✅ Acentos IPA corregidos")
    
    # --- NUEVAS ENTRADAS: Verbos de cocina (Corregidos fonológicamente) ---
    nuevos_verbos = [
        {"concepto": "hervir", "kalfirvach": "kvathel", "forma_final": "kvathel", "pos": "verb", "ipa": "/ˈkva.tʰel/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "kvathati 'hervir' + zéō 'hervir'", "corpus": "Skt. Médicos / Gr. Recetarios"}, "transformacion": ["Adaptación directa"], "derivaciones": []},
        {"concepto": "hornear", "kalfirvach": "pakar", "forma_final": "pakar", "pos": "verb", "ipa": "/ˈpa.kar/", "origen": {"lengua": "Sánscrito/Persa", "raiz_original": "pacati 'cocinar' + pukhtan 'cocer'", "corpus": "Skt. Clásico / Persa Medio"}, "transformacion": ["Convergencia PAC"], "derivaciones": []},
        {"concepto": "mezclar", "kalfirvach": "misal", "forma_final": "misal", "pos": "verb", "ipa": "/ˈmi.sal/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "miśrayati 'mezclar' + mignymi 'mezclar'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["miśra→misa"], "derivaciones": []},
        {"concepto": "cortar", "kalfirvach": "kiras", "forma_final": "kiras", "pos": "verb", "ipa": "/ˈki.ras/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "kṛntati 'cortar' + keírō 'cortar'", "corpus": "Skt. Védico / Gr. Homérico"}, "transformacion": ["kṛt→kir"], "derivaciones": []},
        {"concepto": "pelar", "kalfirvach": "tuvakar", "forma_final": "tuvakar", "pos": "verb", "ipa": "/tu.ˈva.kar/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "tvac 'piel' + derma 'piel'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["tvac→tuva (epéntesis)"], "derivaciones": []},
        {"concepto": "rallar", "kalfirvach": "kharit", "forma_final": "kharit", "pos": "verb", "ipa": "/ˈkʰa.rit/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "kharati 'rascar' + xéō 'raspar'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["Ensordecimiento coda d→t"], "derivaciones": []},
        {"concepto": "batir", "kalfirvach": "mathel", "forma_final": "mathel", "pos": "verb", "ipa": "/ˈma.tʰel/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "mathnāti 'batir' + tarássō 'agitar'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["math→mathe"], "derivaciones": []},
        {"concepto": "amasar", "kalfirvach": "mardar", "forma_final": "mardar", "pos": "verb", "ipa": "/ˈmar.dar/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "mardati 'amasar' + mássō 'amasar'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["mard→mardar"], "derivaciones": []},
        {"concepto": "fermentar", "kalfirvach": "suray", "forma_final": "suray", "pos": "verb", "ipa": "/su.ˈraj/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "sura 'licor fermentado' + zytós 'levadura'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["sura+zyp→suray"], "derivaciones": []},
        {"concepto": "marinar", "kalfirvach": "lunik", "forma_final": "lunik", "pos": "verb", "ipa": "/ˈlu.nik/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "lavana 'sal' + háls 'sal'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["lav+lun→lunik"], "derivaciones": []},
        {"concepto": "glasear", "kalfirvach": "ghrisay", "forma_final": "ghrisay", "pos": "verb", "ipa": "/ˈɣri.saj/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "ghṛta 'grasa/mantequilla' + chrísma 'ungüento'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["ghr→ghri"], "derivaciones": []},
        {"concepto": "escaldar", "kalfirvach": "dahul", "forma_final": "dahul", "pos": "verb", "ipa": "/ˈda.hul/", "origen": {"lengua": "Sánscrito/Persa", "raiz_original": "dahati 'quemar' + dāgh 'marca de quemadura'", "corpus": "Skt. Clásico / Persa Medio"}, "transformacion": ["dah+dag→dahul"], "derivaciones": []},
        {"concepto": "pochar", "kalfirvach": "manday", "forma_final": "manday", "pos": "verb", "ipa": "/man.ˈdaj/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "mandam 'líquido suave' + bradýs 'lento'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["mand+bra→manday"], "derivaciones": []},
        {"concepto": "saltear", "kalfirvach": "plavas", "forma_final": "plavas", "pos": "verb", "ipa": "/ˈpla.vas/", "origen": {"lengua": "Sánscrito/Griego", "raiz_original": "plavate 'flotar/saltar' + hallomai 'saltar'", "corpus": "Skt. Clásico / Gr. Antiguo"}, "transformacion": ["plav+hal→plavas"], "derivaciones": []},
        {"concepto": "gratinar", "kalfirvach": "zarik", "forma_final": "zarik", "pos": "verb", "ipa": "/ˈza.rik/", "origen": {"lengua": "Persa/Sánscrito", "raiz_original": "zar 'oro' + svarṇa 'oro'", "corpus": "Persa Medio / Skt. Clásico"}, "transformacion": ["zar+svar→zarik"], "derivaciones": []}
    ]
    
    if 'comida_y_cocina' in categorias:
        categorias['comida_y_cocina']['entradas'].extend(nuevos_verbos)
        contador_nuevas = len(nuevos_verbos)
        print(f"   ✅ {contador_nuevas} verbos de cocina añadidos")
    else:
        print("   ❌ ERROR: Categoría 'comida_y_cocina' no encontrada.")
        return
    
    # Actualizar metadata
    metadata['version'] = '1.2'
    total_entries = sum(len(cat['entradas']) for cat in categorias.values())
    metadata['total_entries'] = total_entries
    metadata['total_categorias'] = len(categorias)
    
    # Limpieza de contadores redundantes
    if 'total_entradas' in metadata:
        del metadata['total_entradas']
    
    # Guardar archivo
    with open('kalfirvach_lexicon_v1.2.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\n✅ PROCESO COMPLETADO CON ÉXITO")
    print(f"   - Correcciones aplicadas: {contador_correcciones}")
    print(f"   - Nuevos verbos añadidos: {contador_nuevas}")
    print(f"   - Total entradas actual: {total_entries}")
    print(f"   - Versión actualizada a: {metadata['version']}")
    print(f"   - Archivo guardado correctamente.")

if __name__ == '__main__':
    main()
