# -*- coding: utf-8 -*-
"""
Taller de Cálculo Diferencial — Unidad 1: Funciones
Material de apoyo para ayudantía. IER-UNAM.

Referencias:
  [S] Stewart, J. — Precálculo: Matemáticas para el Cálculo, Cap. 2 "Funciones".
  [D] Presentación "Cálculo Diferencial — Unidad 1: Funciones" (Dr. J. G. Rueda, IER-UNAM).

Ejecutar con:  streamlit run app.py
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ----------------------------------------------------------------------------------

st.set_page_config(
    page_title="Taller · Cálculo Diferencial — Unidad 1",
    page_icon="📐",
    layout="wide",
)

AZUL = "#1f4e79"
VERDE = "#7a9a01"
OCRE = "#b8860b"
ROJO = "#a02020"


def nueva_fig(figsize=(5.2, 3.4), xlabel="x", ylabel="y"):
    """Ejes cartesianos con estilo uniforme."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.axhline(0, color="0.25", lw=0.9)
    ax.axvline(0, color="0.25", lw=0.9)
    ax.grid(alpha=0.25, ls=":")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    return fig, ax


def render(bloques):
    """Renderiza una lista de tuplas (tipo, contenido)."""
    for tipo, cont in bloques:
        if tipo == "md":
            st.markdown(cont)
        elif tipo == "tex":
            st.latex(cont)
        elif tipo == "ok":
            st.success(cont)
        elif tipo == "info":
            st.info(cont)
        elif tipo == "warn":
            st.warning(cont)
        elif tipo == "err":
            st.error(cont)
        elif tipo == "fig":
            st.pyplot(cont())
        elif tipo == "div":
            st.markdown("---")


def mostrar_ejercicios(lista, abrir=False):
    for k, ej in enumerate(lista, start=1):
        etiqueta = f"**Ejercicio {k}.** {ej['t']}  ·  _{ej['f']}_"
        with st.expander(etiqueta, expanded=abrir):
            st.markdown("**Enunciado**")
            render(ej["e"])
            st.markdown("---")
            st.markdown("**Solución**")
            render(ej["s"])


def mostrar_ejemplos(lista):
    for k, ex in enumerate(lista, start=1):
        st.markdown(f"##### Ejemplo {k}. {ex['t']}  ·  _{ex['f']}_")
        render(ex["c"])
        st.markdown("")


# ----------------------------------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------------------------------

with st.sidebar:
    st.markdown("### 📐 Taller de ejercicios")
    st.markdown("**Cálculo Diferencial — Unidad 1: Funciones**")
    st.caption("IER–UNAM · Material de ayudantía")
    st.markdown("---")
    abrir_todo = st.checkbox("Abrir todas las soluciones", value=False)
    st.markdown("---")
    st.markdown("**Fuentes**")
    st.caption(
        "**[S]** Stewart, *Precálculo: Matemáticas para el Cálculo*, Cap. 2.\n\n"
        "**[D]** Presentación de la Unidad 1 (Dr. J. G. Rueda)."
    )
    st.markdown("---")
    st.caption(
        "Sugerencia de uso en pizarrón: abrir el enunciado, pedir que lo intenten "
        "3–5 min, y luego desplegar la solución paso a paso."
    )


st.title("Taller de solución de ejercicios — Unidad 1: Funciones")
st.caption(
    "Conceptos, ejemplos resueltos y ejercicios con solución detallada. "
    "Cada ejercicio indica su procedencia (ejercicio y página del Stewart, o diapositiva de la unidad)."
)

TABS = st.tabs([
    "🏠 Inicio",
    "1 · Preliminares",
    "2 · Funciones",
    "3 · Propiedades",
    "4 · Composición e inversa",
    "5 · Tipos y familias",
    "6 · Modelos matemáticos",
    "⚠️ Errores frecuentes",
])


# ==================================================================================
# TAB 0 — INICIO
# ==================================================================================
with TABS[0]:
    st.header("Cómo está organizado este taller")

    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown(
            """
Cada pestaña corresponde a una sección de la Unidad 1 y tiene la misma estructura:

1. **Conceptos** — las definiciones mínimas que se necesitan para resolver, en el mismo
   orden en que aparecen en la presentación del curso.
2. **Ejemplos resueltos** — dos o tres casos modelo, resueltos completos, para explicar
   la técnica antes de que el grupo trabaje.
3. **Ejercicios** — de 5 a 10 problemas con la solución completa dentro de una sección
   desplegable, para no revelarla antes de tiempo.

**Recorrido sugerido para una sesión de 90 minutos**

| Bloque | Contenido | Tiempo |
|---|---|---|
| A | Dominio, rango y evaluación (pestaña 2) | 25 min |
| B | Inyectiva / suprayectiva / biyectiva (pestaña 3) | 20 min |
| C | Composición e inversa (pestaña 4) | 30 min |
| D | Un modelo aplicado (pestaña 6) | 15 min |

La pestaña **Preliminares** sirve como repaso rápido de notación de conjuntos e
intervalos: es el lenguaje con el que se escriben todos los dominios.
"""
        )
    with c2:
        st.info(
            "**Idea central de toda la unidad**\n\n"
            "Una función es una regla que asigna a **cada** entrada **exactamente una** salida.\n\n"
            "Todo lo demás (dominio, rango, inyectividad, inversa) son consecuencias de esa "
            "frase."
        )
        st.success(
            "**Las tres restricciones de dominio**\n\n"
            "• Denominador $\\neq 0$\n\n"
            "• Radicando de raíz par $\\geq 0$\n\n"
            "• Argumento de logaritmo $> 0$"
        )

    st.markdown("---")
    st.subheader("Mapa de la unidad")

    def _fig_mapa():
        fig, ax = plt.subplots(figsize=(10, 2.6))
        ax.axis("off")
        cajas = [
            ("Conjuntos\ne intervalos", 0.5),
            ("Función:\ndominio, rango", 2.4),
            ("Propiedades:\niny/supra/biy", 4.3),
            ("Composición\ne inversa", 6.2),
            ("Familias\nde funciones", 8.1),
            ("Modelos", 9.7),
        ]
        for texto, x in cajas:
            ax.add_patch(plt.Rectangle((x, 0.35), 1.5, 0.8, fc="#eaf0f6",
                                       ec=AZUL, lw=1.4, zorder=2))
            ax.text(x + 0.75, 0.75, texto, ha="center", va="center",
                    fontsize=9, color=AZUL, zorder=3)
        for _, x in cajas[:-1]:
            ax.annotate("", xy=(x + 1.85, 0.75), xytext=(x + 1.5, 0.75),
                        arrowprops=dict(arrowstyle="->", color="0.4"))
        ax.set_xlim(0, 11.5)
        ax.set_ylim(0, 1.5)
        fig.tight_layout()
        return fig

    st.pyplot(_fig_mapa())


# ==================================================================================
# TAB 1 — PRELIMINARES
# ==================================================================================
with TABS[1]:
    st.header("1 · Preliminares: notación y conjuntos")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Símbolos de pertenencia y cuantificadores")
        st.markdown(
            """
| Símbolo | Lectura |
|---|---|
| $a \\in A$ | $a$ pertenece al conjunto $A$ |
| $a \\notin A$ | $a$ no pertenece a $A$ |
| $A \\subseteq B$ | $A$ es subconjunto de $B$ |
| $A \\subset B$ | $A$ es subconjunto **propio** de $B$ |
| $\\varnothing$ | conjunto vacío |
| $\\forall$ | para todo |
| $\\exists$ | existe (al menos uno) |
| $\\exists !$ | existe un único |
| $\\Rightarrow$ | implica |
| $\\Leftrightarrow$ | si y sólo si |
"""
        )
        st.markdown("**Cómo se leen en voz alta**")
        st.latex(r"\forall x \in \mathbb{R},\ x^{2} \ge 0")
        st.caption("«Para todo real $x$, $x^2$ es mayor o igual que cero.»")
        st.latex(r"\exists!\, x \in \mathbb{R}^{+} : x^{2} = 9")
        st.caption("«Existe un único real positivo cuyo cuadrado es 9.» (es $x=3$)")

    with c2:
        st.markdown("#### Conjuntos numéricos")
        st.latex(r"\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}")
        st.markdown(
            """
- $\\mathbb{N}=\\{0,1,2,3,\\dots\\}$
- $\\mathbb{Z}=\\{\\dots,-2,-1,0,1,2,\\dots\\}$
- $\\mathbb{Q}=\\left\\{ \\tfrac{p}{q} \\;\\middle|\\; p,q\\in\\mathbb{Z},\\ q\\neq 0 \\right\\}$
- $\\mathbb{R}=$ racionales $\\cup$ irracionales
- $\\mathbb{C}=\\{a+bi \\mid a,b\\in\\mathbb{R}\\}$

$\\pi \\in \\mathbb{R}$ pero $\\pi \\notin \\mathbb{Q}$;  $\\sqrt{2}\\in\\mathbb{R}$ pero $\\sqrt{2}\\notin\\mathbb{Q}$.
"""
        )
        st.markdown("#### Dos formas de escribir un conjunto")
        st.latex(r"A=\{1,2,3,4,5\} \quad \text{(por extensión: se listan)}")
        st.latex(r"C=\{x\in\mathbb{R} \mid x^{2}<9\}=(-3,3) \quad \text{(por comprensión: regla)}")
        st.warning(
            "**Bien definido.** «Los números grandes» **no** es un conjunto: no hay criterio "
            "de pertenencia. «Los números mayores que 100» **sí** lo es."
        )

    st.markdown("#### Operaciones y notación de intervalos")
    c3, c4 = st.columns(2)
    with c3:
        st.latex(r"A\cup B=\{x \mid x\in A \ \text{o}\ x\in B\}")
        st.latex(r"A\cap B=\{x \mid x\in A \ \text{y}\ x\in B\}")
        st.latex(r"A\setminus B=\{x \mid x\in A \ \text{y}\ x\notin B\}")
        st.markdown("Si $A\\cap B=\\varnothing$, $A$ y $B$ son **disjuntos**.")
    with c4:
        st.markdown(
            """
| Intervalo | Significado |
|---|---|
| $(a,b)$ | $a<x<b$ (abierto) |
| $[a,b]$ | $a\\le x\\le b$ (cerrado) |
| $[a,b)$ | $a\\le x<b$ |
| $(-\\infty,b]$ | $x\\le b$ |
| $[a,+\\infty)$ | $x\\ge a$ |

El $\\infty$ **nunca** lleva corchete: no es un número.
"""
        )

    st.markdown("---")
    st.subheader("Ejemplos resueltos")

    ejemplos_u1 = [
        {
            "t": "Traducir notación a palabras y verificar",
            "f": "[D] diapositiva 4",
            "c": [
                ("md", "Decidir si cada proposición es verdadera."),
                ("tex", r"\text{(a) } 3\in\{1,2,3,4\} \qquad \text{(b) } \exists x\in\mathbb{R}: x^{2}=4 \qquad \text{(c) } \forall x\in\mathbb{R},\ x^{2}>0"),
                ("md",
                 "**(a)** Verdadera: 3 aparece listado en el conjunto.\n\n"
                 "**(b)** Verdadera: basta **exhibir un** testigo, $x=2$ (también $x=-2$). "
                 "El cuantificador $\\exists$ sólo pide uno.\n\n"
                 "**(c)** **Falsa**: $\\forall$ exige que se cumpla para *todos*, y $x=0$ da "
                 "$0^2=0$, que no es $>0$. Un solo contraejemplo tumba un $\\forall$."),
                ("info", "Regla práctica: para probar $\\exists$ se **construye** un ejemplo; "
                         "para refutar $\\forall$ se **construye un contraejemplo**."),
            ],
        },
        {
            "t": "Pasar de comprensión a extensión / intervalo",
            "f": "[D] diapositiva 6",
            "c": [
                ("tex", r"C=\{x\in\mathbb{R} \mid x^{2}<9\}, \qquad D=\{n\in\mathbb{N} \mid n \text{ es par}\}"),
                ("md", "Para $C$: $x^2<9 \\iff |x|<3 \\iff -3<x<3$."),
                ("tex", r"C=(-3,3)"),
                ("md", "Para $D$: los naturales pares son $0,2,4,6,\\dots$"),
                ("tex", r"D=\{0,2,4,6,\dots\}"),
                ("warn", "Ojo con el universo: si fuera $\\{n\\in\\mathbb{Z} \\mid n \\text{ par}\\}$ "
                         "habría que incluir también $-2,-4,\\dots$"),
            ],
        },
        {
            "t": "Unión e intersección de intervalos",
            "f": "[D] diapositivas 8–9",
            "c": [
                ("tex", r"(-\infty,2]\cup[0,+\infty) \qquad \text{y} \qquad (-\infty,3)\cap(1,+\infty)"),
                ("md",
                 "**Unión:** dibujando ambos en la recta, el primero cubre todo hasta 2 y el segundo "
                 "todo desde 0. Se traslapan en $[0,2]$ y juntos no dejan huecos:"),
                ("tex", r"(-\infty,2]\cup[0,+\infty)=\mathbb{R}"),
                ("md", "**Intersección:** hace falta cumplir **las dos** condiciones a la vez: "
                       "$x<3$ **y** $x>1$."),
                ("tex", r"(-\infty,3)\cap(1,+\infty)=(1,3)"),
                ("info", "Truco: la **unión** es «lo que cubre al menos una banda»; la **intersección** "
                         "es «lo que cubre el traslape»."),
            ],
        },
    ]
    mostrar_ejemplos(ejemplos_u1)

    st.markdown("---")
    st.subheader("Ejercicios")

    def _fig_signos():
        fig, ax = plt.subplots(figsize=(6.4, 1.6))
        ax.axhline(0, color="0.25", lw=1.2)
        for x in (-2, 3):
            ax.plot([x], [0], "o", color=ROJO, ms=8, zorder=3)
            ax.annotate(str(x), (x, -0.28), ha="center", color=ROJO)
        ax.text(-4.0, 0.25, "$(+)$", ha="center", fontsize=12, color=VERDE)
        ax.text(0.5, 0.25, "$(-)$", ha="center", fontsize=12, color=ROJO)
        ax.text(4.5, 0.25, "$(+)$", ha="center", fontsize=12, color=VERDE)
        ax.plot([-6, -2], [0, 0], lw=4, color=VERDE, solid_capstyle="butt")
        ax.plot([3, 6], [0, 0], lw=4, color=VERDE, solid_capstyle="butt")
        ax.set_xlim(-6, 6)
        ax.set_ylim(-0.6, 0.6)
        ax.set_yticks([])
        for lado in ("top", "right", "left"):
            ax.spines[lado].set_visible(False)
        ax.set_title(r"Signo de $(x+2)(x-3)$", fontsize=10)
        fig.tight_layout()
        return fig

    ejercicios_u1 = [
        {
            "t": "Escribir un conjunto por extensión",
            "f": "[D] diapositiva 6",
            "e": [("tex", r"E=\{n\in\mathbb{N} \mid n \text{ es par y } n<10\}")],
            "s": [
                ("md", "Se recorre el universo $\\mathbb{N}=\\{0,1,2,\\dots\\}$ y se filtran los que "
                       "cumplen **ambas** condiciones."),
                ("md", "- Pares: $0,2,4,6,8,10,12,\\dots$\n- Menores que 10: se corta en 8."),
                ("tex", r"E=\{0,2,4,6,8\}"),
                ("warn", "Error común: incluir el 10. La condición es $n<10$ estricta. "
                         "Y no olvidar el $0$, que es par y natural."),
            ],
        },
        {
            "t": "¿Es un conjunto bien definido?",
            "f": "[D] diapositiva 6",
            "e": [("md", "Decidir cuáles de las siguientes colecciones son conjuntos bien definidos:\n\n"
                         "(a) los números reales altos  (b) los enteros múltiplos de 7  "
                         "(c) las materias difíciles de la maestría  (d) $\\{x\\in\\mathbb{R} \\mid x^2=-1\\}$")],
            "s": [
                ("md",
                 "El criterio es: **dado un objeto cualquiera, ¿puedo decidir sin ambigüedad si pertenece o no?**\n\n"
                 "**(a)** No. «Alto» no tiene umbral. ¿$1000$ es alto? Depende de quién responda.\n\n"
                 "**(b)** Sí. $n$ pertenece $\\iff n=7k$ para algún $k\\in\\mathbb{Z}$. Criterio verificable.\n\n"
                 "**(c)** No. «Difícil» es subjetivo.\n\n"
                 "**(d)** Sí, y además es el **conjunto vacío**: ningún real al cuadrado da $-1$."),
                ("tex", r"\{x\in\mathbb{R} \mid x^{2}=-1\}=\varnothing"),
                ("info", "El vacío es un conjunto perfectamente legítimo: estar vacío no es estar mal definido."),
            ],
        },
        {
            "t": "Operaciones con intervalos",
            "f": "[D] diapositivas 8–9",
            "e": [("md", "Calcular y expresar el resultado en notación de intervalos:\n\n"
                         "(a) $(-3,0)\\cup(0,3)$  (b) $[0,2]\\cap[3,5]$  "
                         "(c) $\\mathbb{R}\\setminus\\{-1,1\\}$  (d) $\\mathbb{Q}\\cap(\\mathbb{R}\\setminus\\mathbb{Q})$")],
            "s": [
                ("md", "**(a)** Los dos intervalos son abiertos en $0$, así que el $0$ no está en ninguno "
                       "y por tanto tampoco en la unión. Todo lo demás entre $-3$ y $3$ sí está:"),
                ("tex", r"(-3,0)\cup(0,3)=(-3,3)\setminus\{0\}"),
                ("md", "**(b)** No hay ningún número que sea a la vez $\\le 2$ y $\\ge 3$. Son disjuntos:"),
                ("tex", r"[0,2]\cap[3,5]=\varnothing"),
                ("md", "**(c)** Se quitan dos puntos de la recta, lo que la parte en tres pedazos:"),
                ("tex", r"\mathbb{R}\setminus\{-1,1\}=(-\infty,-1)\cup(-1,1)\cup(1,+\infty)"),
                ("md", "**(d)** Un número no puede ser racional e irracional simultáneamente "
                       "(la definición de irracional es *no racional*):"),
                ("tex", r"\mathbb{Q}\cap(\mathbb{R}\setminus\mathbb{Q})=\varnothing"),
                ("info", "El inciso (c) es exactamente la forma en que se escribirá el dominio de "
                         "$g(x)=\\dfrac{1}{x^{2}-1}$ más adelante."),
            ],
        },
        {
            "t": "Igualdad de conjuntos por doble contención",
            "f": "[D] diapositiva 7",
            "e": [("md", "Sean $A=\\{x\\in\\mathbb{R} \\mid x^{2}=1\\}$ y $B=\\{-1,1\\}$. "
                         "Demostrar que $A=B$.")],
            "s": [
                ("md", "Se usa la definición: $A=B \\iff A\\subseteq B$ **y** $B\\subseteq A$."),
                ("md", "**($A\\subseteq B$)** Sea $x\\in A$. Entonces $x^2=1$, es decir"),
                ("tex", r"x^{2}-1=0 \;\Longrightarrow\; (x-1)(x+1)=0 \;\Longrightarrow\; x=1 \ \text{o}\ x=-1"),
                ("md", "En cualquiera de los dos casos $x\\in B$."),
                ("md", "**($B\\subseteq A$)** Hay sólo dos elementos que revisar: "
                       "$(1)^2=1$ ✓ y $(-1)^2=1$ ✓. Los dos están en $A$."),
                ("ok", "Como se cumplen ambas contenciones, $A=B$."),
                ("info", "Este es el esquema estándar de demostración de igualdad de conjuntos, "
                         "y reaparece al probar que $\\operatorname{Ran}(f)=\\operatorname{Cod}(f)$ "
                         "en suprayectividad."),
            ],
        },
        {
            "t": "Resolver una desigualdad cuadrática (preparación para dominios)",
            "f": "[S] método de la Sección 1.7, usado en §2.1 p. 147",
            "e": [("tex", r"\text{Hallar } \{x\in\mathbb{R} \mid x^{2}-x-6 \ge 0\}")],
            "s": [
                ("md", "**Paso 1. Todo de un lado y factorizar.**"),
                ("tex", r"x^{2}-x-6=(x+2)(x-3)\ \ge 0"),
                ("md", "**Paso 2. Raíces (puntos críticos):** $x=-2$ y $x=3$. Dividen la recta en tres zonas."),
                ("md", "**Paso 3. Tabla de signos.** Se prueba un valor de cada zona:"),
                ("md",
                 "| Zona | valor de prueba | $(x+2)$ | $(x-3)$ | producto |\n"
                 "|---|---|---|---|---|\n"
                 "| $x<-2$ | $-3$ | $-$ | $-$ | $+$ |\n"
                 "| $-2<x<3$ | $0$ | $+$ | $-$ | $-$ |\n"
                 "| $x>3$ | $4$ | $+$ | $+$ | $+$ |"),
                ("fig", _fig_signos),
                ("md", "**Paso 4.** Se pide $\\ge 0$, así que se toman las zonas positivas **y** las "
                       "raíces (donde vale exactamente 0):"),
                ("tex", r"\{x \mid x^{2}-x-6\ge 0\}=(-\infty,-2]\cup[3,+\infty)"),
                ("warn", "Si la desigualdad fuera estricta ($>0$), los extremos saldrían: "
                         "$(-\\infty,-2)\\cup(3,+\\infty)$. Esa diferencia decide si el dominio "
                         "lleva corchete o paréntesis."),
            ],
        },
        {
            "t": "Desigualdad con cociente",
            "f": "[S] método de la Sección 1.7, usado en §2.1 p. 147",
            "e": [("tex", r"\text{Hallar } \left\{x\in\mathbb{R} \;\middle|\; \frac{x-2}{x+1}\ \ge\ 0\right\}")],
            "s": [
                ("err", "**No** se multiplica por $(x+1)$: no se sabe su signo y podría voltear la "
                        "desigualdad. Se analiza por signos."),
                ("md", "**Puntos críticos:** el numerador se anula en $x=2$; el denominador en $x=-1$ "
                       "(ahí la expresión **no existe**)."),
                ("md",
                 "| Zona | $(x-2)$ | $(x+1)$ | cociente |\n"
                 "|---|---|---|---|\n"
                 "| $x<-1$ | $-$ | $-$ | $+$ |\n"
                 "| $-1<x<2$ | $-$ | $+$ | $-$ |\n"
                 "| $x>2$ | $+$ | $+$ | $+$ |"),
                ("md", "Se pide $\\ge 0$: se toman las zonas positivas. Se **incluye** $x=2$ "
                       "(el cociente vale 0) y se **excluye** $x=-1$ (no está definido)."),
                ("tex", r"(-\infty,-1)\cup[2,+\infty)"),
                ("info", "Esta es exactamente la cuenta que aparecerá al calcular el dominio de "
                         "$h(x)=\\sqrt{\\dfrac{x-2}{x+1}}$."),
            ],
        },
        {
            "t": "Traducir enunciados matemáticos a notación",
            "f": "[D] diapositiva 4",
            "e": [("md", "Escribir en notación simbólica:\n\n"
                         "(a) todo número real tiene un cubo real  \n"
                         "(b) existe un entero cuyo cuadrado es 16  \n"
                         "(c) el vacío está contenido en cualquier conjunto  \n"
                         "(d) si un número es natural, entonces es entero")],
            "s": [
                ("tex", r"\text{(a)}\quad \forall x\in\mathbb{R},\ \exists\, y\in\mathbb{R}: y=x^{3}"),
                ("tex", r"\text{(b)}\quad \exists\, n\in\mathbb{Z}: n^{2}=16"),
                ("tex", r"\text{(c)}\quad \forall A,\ \varnothing\subseteq A"),
                ("tex", r"\text{(d)}\quad x\in\mathbb{N} \;\Rightarrow\; x\in\mathbb{Z}"),
                ("md", "Observación sobre (b): hay **dos** testigos, $n=4$ y $n=-4$. Si el enunciado "
                       "dijera «existe un **único**» sería falso, y habría que restringir a "
                       "$\\mathbb{Z}^{+}$ para que fuera verdadero:"),
                ("tex", r"\exists!\, n\in\mathbb{Z}^{+}: n^{2}=16"),
                ("info", "En (d), la implicación es precisamente la definición de $\\mathbb{N}\\subseteq\\mathbb{Z}$."),
            ],
        },
    ]
    mostrar_ejercicios(ejercicios_u1, abrir_todo)


# ==================================================================================
# TAB 2 — FUNCIONES
# ==================================================================================
with TABS[2]:
    st.header("2 · Funciones: definición, evaluación, dominio y rango")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Definición")
        st.markdown(
            "Una **función** $f$ de $A$ en $B$ es una regla que asigna a **cada** elemento "
            "$x\\in A$ **exactamente un** elemento $f(x)\\in B$."
        )
        st.latex(r"f\colon A\to B, \qquad x \mapsto f(x)")
        st.markdown(
            """
- $A=\\operatorname{Dom}(f)$: **dominio**, las entradas válidas.
- $B=\\operatorname{Cod}(f)$: **codominio**, dónde se declara que viven las salidas.
- $\\operatorname{Ran}(f)=\\{f(x) \\mid x\\in A\\}\\subseteq B$: **rango**, las salidas que
  la función **efectivamente** produce.
"""
        )
        st.latex(r"\operatorname{Ran}(f)\subseteq \operatorname{Cod}(f)\ \text{ siempre}")
        st.warning(
            "Dos entradas **sí** pueden compartir salida ($f(1)=f(3)$ es legal). "
            "Lo prohibido es que **una** entrada tenga dos salidas, o ninguna."
        )
    with c2:
        st.markdown("#### Dominio natural")
        st.markdown(
            "Si no se declara el dominio, se toma el **conjunto más grande de reales** donde "
            "la fórmula tiene sentido como número real. Tres restricciones:"
        )
        st.latex(r"\text{denominador}\neq 0 \qquad \sqrt[\text{par}]{\ \cdot\ }\ \ge 0 \qquad \log(\cdot)>0")
        st.markdown(
            """
| Función | Dominio natural |
|---|---|
| $f(x)=x^{2}-3x$ | $\\mathbb{R}$ |
| $g(x)=\\dfrac{1}{x-2}$ | $\\mathbb{R}\\setminus\\{2\\}$ |
| $h(x)=\\sqrt{x+4}$ | $[-4,+\\infty)$ |
| $k(x)=\\ln x$ | $(0,+\\infty)$ |
"""
        )
        st.info(
            "**Lectura gráfica:** el dominio es la **sombra sobre el eje $x$**; el rango es la "
            "**sombra sobre el eje $y$**."
        )

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("#### Notación funcional y cociente de diferencias")
        st.markdown(
            "$f(x)$ se lee «$f$ de $x$». Evaluar es **sustituir**: donde diga $x$, se pone lo que entra."
        )
        st.latex(r"\frac{f(x+h)-f(x)}{h}, \qquad h\neq 0")
        st.caption(
            "Cociente de diferencias: cambio promedio de $f$ entre $x$ y $x+h$. "
            "Es la cantidad que, al tomar $h\\to 0$, se vuelve la derivada. "
            "([S] Ejemplo 4, p. 145)"
        )
        st.error("$f(2x)\\neq 2f(x)$ en general. Si $f(x)=x^2$: $f(2x)=4x^2=4f(x)$.")
    with c4:
        st.markdown("#### Prueba de la línea vertical")
        st.markdown(
            "Una curva del plano es la gráfica de una función **si y sólo si** toda recta "
            "vertical $x=c$ la corta **a lo sumo una vez**."
        )

        def _fig_vlt():
            fig, axes = plt.subplots(1, 2, figsize=(6.4, 2.8))
            x = np.linspace(-1.6, 1.6, 300)
            axes[0].plot(x, x ** 2, color=AZUL, lw=2)
            axes[0].axvline(0.8, color=OCRE, ls="--")
            axes[0].plot([0.8], [0.64], "o", color=VERDE, ms=7)
            axes[0].set_title(r"$y=x^{2}$: sí es función", fontsize=9, color=VERDE)
            t = np.linspace(0, 2 * np.pi, 400)
            axes[1].plot(np.cos(t), np.sin(t), color=AZUL, lw=2)
            axes[1].axvline(0.5, color=OCRE, ls="--")
            axes[1].plot([0.5, 0.5], [np.sqrt(0.75), -np.sqrt(0.75)], "o", color=ROJO, ms=7)
            axes[1].set_title(r"$x^{2}+y^{2}=1$: no es función", fontsize=9, color=ROJO)
            for a in axes:
                a.axhline(0, color="0.3", lw=0.8)
                a.axvline(0, color="0.3", lw=0.8)
                a.grid(alpha=0.2, ls=":")
                a.set_aspect("equal", adjustable="datalim")
            fig.tight_layout()
            return fig

        st.pyplot(_fig_vlt())

    st.markdown("---")
    st.subheader("Ejemplos resueltos")

    def _fig_x2mas4():
        fig, ax = nueva_fig()
        x = np.linspace(-4, 4, 400)
        ax.plot(x, x ** 2 + 4, color=AZUL, lw=2)
        ax.axhline(4, color=VERDE, ls="--", lw=1.2)
        ax.plot([0], [4], "o", color=VERDE, ms=7)
        ax.annotate(r"mínimo $(0,4)$", (0, 4), textcoords="offset points",
                    xytext=(12, -18), color=VERDE)
        ax.set_title(r"$f(x)=x^{2}+4$   ·   $\mathrm{Ran}(f)=[4,\infty)$", fontsize=10)
        fig.tight_layout()
        return fig

    ejemplos_u2 = [
        {
            "t": "Analizar una función completa",
            "f": "[S] Ejemplo 1, p. 144",
            "c": [
                ("md", "Sea $f(x)=x^{2}+4$. Describir la regla, evaluar, y hallar dominio y rango."),
                ("md", "**Regla en palabras:** «elevar al cuadrado, luego sumar 4»."),
                ("md", "**Evaluación** (sustituir en la fórmula):"),
                ("tex", r"f(3)=3^{2}+4=13, \qquad f(-2)=(-2)^{2}+4=8, \qquad f(\sqrt{5})=(\sqrt{5})^{2}+4=9"),
                ("md", "**Dominio:** la fórmula no tiene denominadores, raíces ni logaritmos; se puede "
                       "evaluar en cualquier real."),
                ("tex", r"\operatorname{Dom}(f)=\mathbb{R}"),
                ("md", "**Rango:** hay que razonar *hacia atrás*, desde las salidas. Para todo real, "
                       "$x^{2}\\ge 0$, entonces:"),
                ("tex", r"x^{2}\ge 0 \;\Longrightarrow\; x^{2}+4\ge 4 \;\Longrightarrow\; f(x)\ge 4"),
                ("md", "Y todo $y\\ge 4$ se alcanza: tomando $x=\\sqrt{y-4}$ se obtiene $f(x)=y$. Por tanto:"),
                ("tex", r"\operatorname{Ran}(f)=[4,+\infty)"),
                ("fig", _fig_x2mas4),
                ("info", "Para el rango siempre hay dos mitades: (i) acotar $f(x)$, (ii) mostrar que "
                         "toda cota se alcanza. Sin (ii) sólo se probó una contención."),
            ],
        },
        {
            "t": "Cociente de diferencias",
            "f": "[S] Ejemplo 4, p. 145",
            "c": [
                ("md", "Si $f(x)=2x^{2}+3x-1$, calcular $f(a)$, $f(a+h)$ y "
                       "$\\dfrac{f(a+h)-f(a)}{h}$, con $h\\neq 0$."),
                ("tex", r"f(a)=2a^{2}+3a-1"),
                ("md", "Para $f(a+h)$ se sustituye **todo el bloque** $a+h$ donde iba $x$, y se expande:"),
                ("tex", r"f(a+h)=2(a+h)^{2}+3(a+h)-1=2(a^{2}+2ah+h^{2})+3a+3h-1"),
                ("tex", r"f(a+h)=2a^{2}+4ah+2h^{2}+3a+3h-1"),
                ("md", "Ahora la resta. Los términos **sin $h$** se cancelan (eso siempre pasa, y es la "
                       "señal de que la cuenta va bien):"),
                ("tex", r"f(a+h)-f(a)=\bigl(2a^{2}+4ah+2h^{2}+3a+3h-1\bigr)-\bigl(2a^{2}+3a-1\bigr)=4ah+2h^{2}+3h"),
                ("md", "Se factoriza $h$ y se cancela (legal porque $h\\neq0$):"),
                ("tex", r"\frac{f(a+h)-f(a)}{h}=\frac{h(4a+2h+3)}{h}=4a+2h+3"),
                ("ok", "Si ahora se hace $h\\to 0$ se obtiene $4a+3$, que es la derivada $f'(a)$. "
                       "Este ejercicio es el puente entre precálculo y cálculo."),
            ],
        },
        {
            "t": "Hallar dominios",
            "f": "[S] Ejemplo 6, pp. 146–147",
            "c": [
                ("tex", r"\text{(a) } f(x)=\frac{1}{x^{2}-x} \qquad \text{(b) } g(x)=\sqrt{9-x^{2}} \qquad \text{(c) } h(t)=\frac{t}{\sqrt{t+1}}"),
                ("md", "**(a)** Restricción: denominador $\\neq 0$. Se factoriza:"),
                ("tex", r"x^{2}-x=x(x-1)=0 \iff x=0 \ \text{o}\ x=1"),
                ("tex", r"\operatorname{Dom}(f)=\mathbb{R}\setminus\{0,1\}=(-\infty,0)\cup(0,1)\cup(1,+\infty)"),
                ("md", "**(b)** Restricción: radicando $\\ge 0$ (raíz de índice par)."),
                ("tex", r"9-x^{2}\ge 0 \iff x^{2}\le 9 \iff -3\le x\le 3"),
                ("tex", r"\operatorname{Dom}(g)=[-3,3]"),
                ("md", "**(c)** Aquí se acumulan **dos** restricciones: la raíz pide $t+1\\ge 0$, pero "
                       "además está en el denominador, así que no puede valer 0. La condición fuerte gana:"),
                ("tex", r"t+1>0 \iff t>-1 \qquad\Longrightarrow\qquad \operatorname{Dom}(h)=(-1,+\infty)"),
                ("warn", "El caso (c) es el más pedido en examen. Raíz **sola**: $\\ge$. Raíz en el "
                         "**denominador**: $>$ estricto."),
            ],
        },
    ]
    mostrar_ejemplos(ejemplos_u2)

    st.markdown("---")
    st.subheader("Ejercicios")

    def _fig_raiz_x_menos_2():
        fig, ax = nueva_fig()
        x = np.linspace(2, 8, 300)
        ax.plot(x, np.sqrt(x - 2), color=AZUL, lw=2)
        ax.plot([2], [0], "o", color=AZUL, ms=8)
        ax.annotate(r"$(2,0)$", (2, 0), textcoords="offset points", xytext=(8, 8), color=AZUL)
        ax.set_xlim(-1, 8)
        ax.set_ylim(-1, 3)
        ax.set_title(r"$f(x)=\sqrt{x-2}$", fontsize=10)
        fig.tight_layout()
        return fig

    def _fig_torricelli():
        fig, ax = nueva_fig(xlabel="t (min)", ylabel="V (gal)")
        t = np.linspace(0, 20, 300)
        ax.plot(t, 50 * (1 - t / 20) ** 2, color=AZUL, lw=2)
        for tt in (0, 5, 10, 15, 20):
            ax.plot([tt], [50 * (1 - tt / 20) ** 2], "o", color=OCRE, ms=6)
        ax.set_title("Ley de Torricelli", fontsize=10)
        ax.set_xlim(-1, 21)
        ax.set_ylim(-3, 55)
        fig.tight_layout()
        return fig

    def _fig_internet():
        fig, ax = nueva_fig(xlabel="x (precio de los libros, $)", ylabel="C (costo total, $)")
        x1 = np.linspace(0, 100, 200)
        x2 = np.linspace(100, 160, 200)
        ax.plot(x1, x1 + 15, color=AZUL, lw=2)
        ax.plot(x2, x2, color=VERDE, lw=2)
        ax.plot([100], [115], "o", mfc="white", mec=AZUL, ms=8)
        ax.plot([100], [100], "o", color=VERDE, ms=8)
        ax.set_title("Costo con envío: salto hacia abajo en $x=100$", fontsize=10)
        ax.set_xlim(0, 160)
        ax.set_ylim(0, 180)
        fig.tight_layout()
        return fig

    ejercicios_u2 = [
        {
            "t": "Evaluar una función en varios puntos",
            "f": "[S] Ejercicio 17, p. 149",
            "e": [("md", "Sea $f(x)=x^{2}+6$. Evaluar $f(-3)$, $f(3)$, $f(0)$, "
                         "$f\\!\\left(\\tfrac{1}{2}\\right)$ y $f(10)$.")],
            "s": [
                ("md", "Evaluar es sustituir. Cuidado con el signo dentro del cuadrado."),
                ("tex", r"f(-3)=(-3)^{2}+6=9+6=15"),
                ("tex", r"f(3)=3^{2}+6=9+6=15"),
                ("tex", r"f(0)=0^{2}+6=6"),
                ("tex", r"f\!\left(\tfrac{1}{2}\right)=\left(\tfrac{1}{2}\right)^{2}+6=\tfrac{1}{4}+6=\tfrac{25}{4}"),
                ("tex", r"f(10)=10^{2}+6=106"),
                ("info", "Nótese que $f(-3)=f(3)$: dos entradas distintas con la misma salida. Es "
                         "perfectamente válido, y es justo lo que hará que esta función **no** sea "
                         "inyectiva (pestaña 3)."),
                ("err", "$(-3)^2=9$, **no** $-9$. El paréntesis es parte del dato: $-3^2$ significa "
                        "$-(3^2)=-9$, que es otra cosa."),
            ],
        },
        {
            "t": "Evaluar una función racional (incluyendo un punto fuera del dominio)",
            "f": "[S] Ejercicio 21, p. 149",
            "e": [("md", "Sea $g(x)=\\dfrac{1-x}{1+x}$. Evaluar $g(2)$, $g(-2)$, "
                         "$g\\!\\left(\\tfrac{1}{2}\\right)$, $g(a)$, $g(a-1)$ y $g(-1)$.")],
            "s": [
                ("tex", r"g(2)=\frac{1-2}{1+2}=\frac{-1}{3}=-\frac{1}{3}"),
                ("tex", r"g(-2)=\frac{1-(-2)}{1+(-2)}=\frac{3}{-1}=-3"),
                ("tex", r"g\!\left(\tfrac{1}{2}\right)=\frac{1-\tfrac12}{1+\tfrac12}=\frac{\tfrac12}{\tfrac32}=\frac{1}{3}"),
                ("tex", r"g(a)=\frac{1-a}{1+a}"),
                ("md", "Para $g(a-1)$ se sustituye el bloque completo y se simplifica:"),
                ("tex", r"g(a-1)=\frac{1-(a-1)}{1+(a-1)}=\frac{1-a+1}{a}=\frac{2-a}{a}"),
                ("md", "Para $g(-1)$:"),
                ("tex", r"g(-1)=\frac{1-(-1)}{1+(-1)}=\frac{2}{0}"),
                ("err", "**$g(-1)$ no existe.** No se escribe «$=\\infty$»: simplemente $-1$ no "
                        "pertenece al dominio, $\\operatorname{Dom}(g)=\\mathbb{R}\\setminus\\{-1\\}$."),
                ("info", "Observación para $g(a-1)$: el resultado $\\tfrac{2-a}{a}$ exige $a\\neq0$, "
                         "que es justamente $a-1\\neq-1$. La restricción viaja con la sustitución."),
            ],
        },
        {
            "t": "Función definida por tramos",
            "f": "[S] Ejercicio 27, p. 150",
            "e": [
                ("md", "Evaluar $f(-2)$, $f(-1)$, $f(0)$, $f(1)$ y $f(2)$ para"),
                ("tex", r"f(x)=\begin{cases} x^{2} & \text{si } x<0 \\[4pt] x+1 & \text{si } x\ge 0 \end{cases}"),
            ],
            "s": [
                ("md", "**El procedimiento tiene dos pasos siempre:** primero se decide *en qué tramo* "
                       "cae la entrada, y sólo después se aplica la fórmula de ese tramo."),
                ("md", "- $-2<0$ → primer tramo: $f(-2)=(-2)^{2}=4$\n"
                       "- $-1<0$ → primer tramo: $f(-1)=(-1)^{2}=1$\n"
                       "- $0\\ge 0$ → **segundo** tramo: $f(0)=0+1=1$\n"
                       "- $1\\ge 0$ → segundo tramo: $f(1)=1+1=2$\n"
                       "- $2\\ge 0$ → segundo tramo: $f(2)=2+1=3$"),
                ("ok", r"$f(-2)=4,\quad f(-1)=1,\quad f(0)=1,\quad f(1)=2,\quad f(2)=3$"),
                ("warn", "El punto delicado es $x=0$: la desigualdad $x\\ge0$ lleva el «igual», así que "
                         "el $0$ pertenece al **segundo** tramo. Si se usa el primero por descuido se "
                         "obtiene $0$ en lugar de $1$."),
                ("info", "Es una función perfectamente legítima aunque su regla tenga varios casos: "
                         "cada entrada sigue teniendo **una sola** salida."),
            ],
        },
        {
            "t": "$f(x+2)$ contra $f(x)+f(2)$",
            "f": "[S] Ejercicio 31, p. 150",
            "e": [("md", "Sea $f(x)=x^{2}+1$. Calcular $f(x+2)$ y $f(x)+f(2)$, y comparar.")],
            "s": [
                ("md", "**$f(x+2)$:** entra el bloque $x+2$ completo."),
                ("tex", r"f(x+2)=(x+2)^{2}+1=x^{2}+4x+4+1=x^{2}+4x+5"),
                ("md", "**$f(x)+f(2)$:** son dos evaluaciones separadas que después se suman."),
                ("tex", r"f(2)=2^{2}+1=5 \qquad\Longrightarrow\qquad f(x)+f(2)=(x^{2}+1)+5=x^{2}+6"),
                ("err", r"$f(x+2)=x^{2}+4x+5 \;\neq\; x^{2}+6=f(x)+f(2)$"),
                ("md", "Difieren en $4x-1$. Coinciden sólo si $4x-1=0$, es decir $x=\\tfrac14$."),
                ("info", "Moraleja: $f$ **no** es un factor que se distribuya. $f(a+b)\\neq f(a)+f(b)$ "
                         "salvo en casos muy particulares (las funciones lineales sin término "
                         "independiente, $f(x)=mx$). El mismo error aparece con "
                         "$\\sqrt{a+b}\\neq\\sqrt a+\\sqrt b$."),
            ],
        },
        {
            "t": "Cociente de diferencias de una función racional",
            "f": "[S] bloque 35–42, p. 150",
            "e": [("md", "Para $f(x)=\\dfrac{1}{x+1}$, hallar $f(a)$, $f(a+h)$ y el cociente de "
                         "diferencias $\\dfrac{f(a+h)-f(a)}{h}$, con $h\\neq 0$.")],
            "s": [
                ("tex", r"f(a)=\frac{1}{a+1}, \qquad f(a+h)=\frac{1}{a+h+1}"),
                ("md", "**Paso 1. Restar con común denominador.** El común denominador es el producto:"),
                ("tex", r"f(a+h)-f(a)=\frac{1}{a+h+1}-\frac{1}{a+1}=\frac{(a+1)-(a+h+1)}{(a+h+1)(a+1)}"),
                ("md", "**Paso 2. Simplificar el numerador** (aquí se cancela casi todo):"),
                ("tex", r"(a+1)-(a+h+1)=a+1-a-h-1=-h"),
                ("tex", r"f(a+h)-f(a)=\frac{-h}{(a+h+1)(a+1)}"),
                ("md", "**Paso 3. Dividir entre $h$**, que es lo mismo que multiplicar por $1/h$:"),
                ("tex", r"\frac{f(a+h)-f(a)}{h}=\frac{-h}{h\,(a+h+1)(a+1)}=\frac{-1}{(a+h+1)(a+1)}"),
                ("ok", "El $h$ del numerador **siempre** debe cancelarse. Si no se cancela, hay un "
                       "error algebraico: sin cancelar, el límite $h\\to0$ daría $0/0$."),
                ("info", "Al tomar $h\\to 0$: $-\\dfrac{1}{(a+1)^{2}}$, que es la derivada de "
                         "$\\dfrac{1}{x+1}$ en $x=a$."),
            ],
        },
        {
            "t": "Dominios naturales (tres restricciones combinadas)",
            "f": "[S] bloque 43–64, p. 150",
            "e": [("md", "Hallar el dominio natural de:\n\n"
                         "(a) $f(x)=\\dfrac{x-4}{x^{2}+x-6}$  \n"
                         "(b) $g(x)=\\sqrt{7-3x}$  \n"
                         "(c) $k(x)=\\dfrac{\\sqrt{x+2}}{x-3}$")],
            "s": [
                ("md", "**(a)** Sólo hay restricción de denominador. Se factoriza:"),
                ("tex", r"x^{2}+x-6=(x+3)(x-2)=0 \iff x=-3 \ \text{o}\ x=2"),
                ("tex", r"\operatorname{Dom}(f)=(-\infty,-3)\cup(-3,2)\cup(2,+\infty)"),
                ("warn", "Que el numerador se anule en $x=4$ **no** afecta el dominio: $f(4)=0$ es una "
                         "salida perfectamente válida. Sólo el denominador restringe."),
                ("md", "**(b)** Raíz de índice par: radicando $\\ge0$."),
                ("tex", r"7-3x\ge 0 \iff 7\ge 3x \iff x\le \tfrac{7}{3}"),
                ("tex", r"\operatorname{Dom}(g)=\left(-\infty,\tfrac{7}{3}\right]"),
                ("err", "Al dividir entre $-3$ **se voltea** la desigualdad. Escribirlo como arriba "
                        "(pasando el $3x$ del otro lado) evita el error."),
                ("md", "**(c)** Dos restricciones **independientes** que se **intersecan**:"),
                ("tex", r"\text{raíz: } x+2\ge 0 \iff x\ge -2 \qquad\text{y}\qquad \text{denominador: } x-3\neq 0 \iff x\neq 3"),
                ("tex", r"\operatorname{Dom}(k)=[-2,+\infty)\setminus\{3\}=[-2,3)\cup(3,+\infty)"),
                ("info", "Cuando hay varias restricciones se **intersecan**, nunca se unen: hay que "
                         "cumplirlas todas a la vez."),
            ],
        },
        {
            "t": "Dominio, codominio y rango, con gráfica",
            "f": "[D] diapositiva 23 (Ejercicio 1 de la unidad)",
            "e": [("md", "Sea $f(x)=\\sqrt{x-2}$. Determinar el dominio natural, el codominio "
                         "declarado $\\mathbb{R}$ y el rango. Graficar.")],
            "s": [
                ("md", "**Dominio.** Para que $\\sqrt{x-2}$ sea un número real:"),
                ("tex", r"x-2\ge 0 \iff x\ge 2 \qquad\Longrightarrow\qquad \operatorname{Dom}(f)=[2,+\infty)"),
                ("md", "**Codominio.** Es un dato **declarado**, no calculado. Aquí se declaró "
                       "$\\operatorname{Cod}(f)=\\mathbb{R}$."),
                ("md", "**Rango.** Dos partes:"),
                ("md", "*(i) Cota:* para $x\\ge2$ se tiene $x-2\\ge 0$, y la raíz cuadrada principal "
                       "nunca es negativa, así que $f(x)\\ge 0$. Entonces "
                       "$\\operatorname{Ran}(f)\\subseteq[0,+\\infty)$."),
                ("md", "*(ii) Alcance:* sea $y\\ge0$ arbitrario. Se propone $x=y^{2}+2$. Como "
                       "$y^2\\ge0$, se cumple $x\\ge2$, o sea $x\\in\\operatorname{Dom}(f)$, y además:"),
                ("tex", r"f(y^{2}+2)=\sqrt{(y^{2}+2)-2}=\sqrt{y^{2}}=|y|=y \quad (\text{pues } y\ge 0)"),
                ("tex", r"\operatorname{Ran}(f)=[0,+\infty)"),
                ("fig", _fig_raiz_x_menos_2),
                ("info", "Aquí $\\operatorname{Ran}(f)=[0,\\infty)\\subsetneq\\mathbb{R}=\\operatorname{Cod}(f)$: "
                         "la función **no** es suprayectiva con ese codominio. Se retoma en la pestaña 3."),
            ],
        },
        {
            "t": "Modelo con dominio físico: Ley de Torricelli",
            "f": "[S] Ejercicio 71, p. 151",
            "e": [
                ("md", "Un tanque contiene 50 galones de agua que se vacía en 20 minutos por una fuga. "
                       "El volumen restante después de $t$ minutos es"),
                ("tex", r"V(t)=50\left(1-\frac{t}{20}\right)^{2}, \qquad 0\le t\le 20"),
                ("md", "(a) Hallar $V(0)$ y $V(20)$. (b) Interpretar. (c) Tabular para "
                       "$t=0,5,10,15,20$."),
            ],
            "s": [
                ("md", "**(a)** Sustitución directa:"),
                ("tex", r"V(0)=50\left(1-0\right)^{2}=50 \qquad V(20)=50\left(1-\tfrac{20}{20}\right)^{2}=50(0)^{2}=0"),
                ("md", "**(b)** $V(0)=50$ gal es el volumen **inicial**: el tanque lleno. $V(20)=0$ dice "
                       "que a los 20 minutos el tanque está **vacío**, que es exactamente la condición "
                       "que da el enunciado. El modelo es consistente."),
                ("md", "**(c)** Tabla:"),
                ("md",
                 "| $t$ (min) | cálculo | $V(t)$ (gal) |\n"
                 "|---|---|---|\n"
                 "| 0 | $50(1)^2$ | 50 |\n"
                 "| 5 | $50(0.75)^2$ | 28.125 |\n"
                 "| 10 | $50(0.5)^2$ | 12.5 |\n"
                 "| 15 | $50(0.25)^2$ | 3.125 |\n"
                 "| 20 | $50(0)^2$ | 0 |"),
                ("fig", _fig_torricelli),
                ("md", "**Interpretación física de la forma de la curva:** en los primeros 5 minutos se "
                       "pierden $50-28.125=21.9$ gal; en los últimos 5 sólo $3.125$ gal. El tanque se "
                       "vacía mucho más rápido al principio, porque la presión sobre la fuga es mayor "
                       "cuando hay más columna de agua."),
                ("warn", "**El dominio está restringido por la física, no por el álgebra.** La fórmula "
                         "$50(1-t/20)^2$ tiene sentido algebraico para todo real, pero para $t>20$ "
                         "predeciría volumen creciente en un tanque ya vacío. Por eso el enunciado "
                         "impone $0\\le t\\le 20$."),
            ],
        },
        {
            "t": "Función por tramos aplicada: compras por Internet",
            "f": "[S] Ejercicio 77, p. 151",
            "e": [
                ("md", "Una librería cobra \\$15 de envío por pedidos de menos de \\$100, y envío "
                       "gratis desde \\$100. El costo total es"),
                ("tex", r"C(x)=\begin{cases} x+15 & \text{si } x<100 \\[4pt] x & \text{si } x\ge 100 \end{cases}"),
                ("md", "(a) Hallar $C(75)$, $C(90)$, $C(100)$ y $C(105)$. (b) Interpretar."),
            ],
            "s": [
                ("md", "**(a)** Se identifica el tramo y luego se aplica la fórmula:"),
                ("md", "- $75<100$ → $C(75)=75+15=90$\n"
                       "- $90<100$ → $C(90)=90+15=105$\n"
                       "- $100\\ge100$ → **segundo tramo**: $C(100)=100$\n"
                       "- $105\\ge100$ → $C(105)=105$"),
                ("md", "**(b)** Cada valor es lo que realmente paga el cliente, libros más envío."),
                ("fig", _fig_internet),
                ("ok", "**Lo interesante:** $C(90)=105$ pero $C(100)=100$. Comprando **más** libros "
                       "(\\$100 en vez de \\$90) se paga **menos** en total. Un cliente racional que "
                       "lleva \\$90 debería agregar \\$10 de libros y ahorrar \\$5."),
                ("info", "Gráficamente hay un **salto hacia abajo** en $x=100$: punto hueco en "
                         "$(100,115)$ y punto lleno en $(100,100)$. Es una discontinuidad de salto, "
                         "concepto que se formaliza en la Unidad 2."),
            ],
        },
        {
            "t": "Prueba de la línea vertical",
            "f": "[D] diapositiva 16 · [S] §2.2, p. 152",
            "e": [("md", "Decidir cuáles de estas curvas definen $y$ como función de $x$:\n\n"
                         "(a) $y=x^{2}$  (b) $x^{2}+y^{2}=1$  (c) $y^{2}=x$  (d) $y=|x|$")],
            "s": [
                ("md", "**Criterio:** toda vertical $x=c$ debe cortar la curva **a lo sumo una vez**. "
                       "Algebraicamente: al despejar $y$ no debe salir un $\\pm$."),
                ("md", "**(a) Sí.** $y=x^2$ ya está despejada; cada $x$ produce un solo valor."),
                ("md", "**(b) No.** Al despejar:"),
                ("tex", r"y^{2}=1-x^{2} \;\Longrightarrow\; y=\pm\sqrt{1-x^{2}}"),
                ("md", "Para $x=0$ hay dos puntos, $y=1$ y $y=-1$. La vertical $x=0$ corta dos veces."),
                ("md", "**(c) No.** $y=\\pm\\sqrt{x}$: para $x=4$ salen $y=2$ y $y=-2$."),
                ("md", "**(d) Sí.** El valor absoluto está definido por tramos pero asigna un único "
                       "valor a cada $x$."),
                ("info", "Las que fallan **sí** se pueden partir en **ramas** que son funciones: la "
                         "circunferencia se separa en $y=\\sqrt{1-x^2}$ (semicírculo superior) y "
                         "$y=-\\sqrt{1-x^2}$ (inferior). Se retoma en la pestaña 5 con funciones "
                         "implícitas."),
                ("warn", "No confundir con la prueba de la línea **horizontal**, que sirve para "
                         "inyectividad, no para ser función."),
            ],
        },
    ]
    mostrar_ejercicios(ejercicios_u2, abrir_todo)


# ==================================================================================
# TAB 3 — PROPIEDADES
# ==================================================================================
# ==================================================================================
# TAB 3 — PROPIEDADES
# (reemplaza íntegramente el bloque `with TABS[3]:` del app.py)
# ==================================================================================
with TABS[3]:
    st.header("3 · Propiedades: inyectiva, suprayectiva, biyectiva")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### Inyectiva (uno a uno)")
        st.latex(r"x_{1}\neq x_{2} \;\Rightarrow\; f(x_{1})\neq f(x_{2})")
        st.markdown("Equivalente (contrapositivo), y es **la forma que se usa para demostrar**:")
        st.latex(r"f(x_{1})=f(x_{2}) \;\Rightarrow\; x_{1}=x_{2}")
        st.markdown("**Línea horizontal:** corta a lo sumo **1** vez.")
        st.info("**Para probar:** suponer $f(x_1)=f(x_2)$ y llegar a $x_1=x_2$.\n\n"
                "**Para refutar:** exhibir un contraejemplo concreto.")
        st.caption(
            "Nota de lectura: Stewart llama a esta propiedad **«uno a uno»** (§2.7, p. 199) y "
            "no usa la palabra *inyectiva*. Son lo mismo."
        )
    with c2:
        st.markdown("#### Suprayectiva (sobre)")
        st.latex(r"\forall y\in B,\ \exists x\in A : f(x)=y")
        st.markdown("Equivalente:")
        st.latex(r"\operatorname{Ran}(f)=\operatorname{Cod}(f)")
        st.markdown("**Línea horizontal:** corta al menos **1** vez (para toda altura en $B$).")
        st.info("**Para probar:** tomar $y\\in B$ arbitrario y **construir** explícitamente el $x$.\n\n"
                "**Para refutar:** exhibir un $y$ sin preimagen.")
        st.caption(
            "Stewart **no** trata suprayectividad: le basta la inyectividad porque siempre toma "
            "como codominio el rango. Por eso los ejercicios del libro se enuncian aquí con el "
            "codominio **declarado**."
        )
    with c3:
        st.markdown("#### Biyectiva")
        st.latex(r"\forall y\in B,\ \exists!\, x\in A : f(x)=y")
        st.markdown("Inyectiva **y** suprayectiva a la vez. **Línea horizontal:** exactamente **1** vez.")
        st.success("Es **la** condición para que exista la inversa $f^{-1}\\colon B\\to A$.")
        st.caption(
            "Criterio rápido del libro (p. 200): **toda función creciente y toda función "
            "decreciente es uno a uno**. Sirve para justificar inyectividad sin álgebra."
        )

    st.markdown(
        """
| Tipo | Línea horizontal | Condición de rango |
|---|---|---|
| Inyectiva | $\\le 1$ intersección | $\\operatorname{Ran}(f)\\subseteq B$ |
| Suprayectiva | $\\ge 1$ intersección | $\\operatorname{Ran}(f)=B$ |
| Biyectiva | $=1$ intersección | $\\operatorname{Ran}(f)=B$ y valores únicos |
"""
    )

    st.warning(
        "**El dominio y el codominio son parte de la función.** La *misma fórmula* $x^2$ puede ser "
        "ninguna de las tres, sólo suprayectiva, o biyectiva, según cómo se declaren $A$ y $B$. "
        "Los ejercicios 2 y 3 de esta pestaña son exactamente ese contraste."
    )

    st.markdown("#### Igualdad de funciones, álgebra de funciones y transformaciones")
    c4, c5 = st.columns(2)
    with c4:
        st.markdown("**Igualdad.** $f=g$ si y sólo si:")
        st.latex(r"\text{(i) } \operatorname{Dom}(f)=\operatorname{Dom}(g) \qquad \text{(ii) } f(x)=g(x)\ \ \forall x")
        st.markdown("**Álgebra de funciones** ([S] p. 191). Con $A=\\operatorname{Dom}(f)$, "
                    "$B=\\operatorname{Dom}(g)$:")
        st.latex(r"(f+g)(x)=f(x)+g(x), \qquad \operatorname{Dom}=A\cap B")
        st.latex(r"(f-g)(x)=f(x)-g(x), \qquad \operatorname{Dom}=A\cap B")
        st.latex(r"(fg)(x)=f(x)\,g(x), \qquad \operatorname{Dom}=A\cap B")
        st.latex(r"\left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}, \quad \operatorname{Dom}=\{x\in A\cap B : g(x)\neq 0\}")
        st.warning(
            "La resta **no** es conmutativa: $(f-g)(x)=-(g-f)(x)$. Y $f/g$ y $g/f$ tienen "
            "**dominios distintos**, porque se excluyen ceros de funciones distintas."
        )
    with c5:
        st.markdown("**Transformaciones** ([S] §2.5)")
        st.markdown(
            """
| Expresión | Efecto |
|---|---|
| $f(x)+c$ | traslación vertical $\\uparrow c$ |
| $f(x)-c$ | traslación vertical $\\downarrow c$ |
| $f(x-c)$ | traslación horizontal $\\rightarrow c$ |
| $f(x+c)$ | traslación horizontal $\\leftarrow c$ |
| $cf(x),\\ c>1$ | alargamiento **vertical** factor $c$ |
| $cf(x),\\ 0<c<1$ | contracción **vertical** factor $c$ |
| $f(cx),\\ c>1$ | contracción **horizontal** factor $1/c$ |
| $f(cx),\\ 0<c<1$ | alargamiento **horizontal** factor $1/c$ |
| $-f(x)$ | reflexión en el eje $x$ |
| $f(-x)$ | reflexión en el eje $y$ |
| $\\lvert f(x)\\rvert$ | refleja hacia arriba lo que está bajo el eje $x$ |
"""
        )
        st.caption(
            "Lo contraintuitivo, y son dos cosas distintas: $f(x-c)$ mueve a la **derecha**, "
            "y $f(cx)$ con $c>1$ **contrae** en vez de alargar."
        )

    st.markdown("---")
    st.subheader("Ejemplos resueltos")

    def _fig_horizontal():
        fig, axes = plt.subplots(1, 3, figsize=(9.5, 2.9))
        x = np.linspace(-2.2, 2.2, 400)
        datos = [
            (x ** 2, r"$x^{2}$ en $\mathbb{R}$: no inyectiva", ROJO, 2.0),
            (np.exp(x) - 2, r"$e^{x}-2$: sólo inyectiva", VERDE, 0.8),
            (x ** 3, r"$x^{3}$ en $\mathbb{R}$: biyectiva", AZUL, 2.0),
        ]
        for a, (y, tit, col, h) in zip(axes, datos):
            a.plot(x, y, color=AZUL, lw=2)
            a.axhline(h, color=OCRE, ls="--", lw=1.3)
            a.set_title(tit, fontsize=8.5, color=col)
            a.axhline(0, color="0.3", lw=0.8)
            a.axvline(0, color="0.3", lw=0.8)
            a.grid(alpha=0.2, ls=":")
            a.set_ylim(-4, 5)
        fig.tight_layout()
        return fig

    ejemplos_u3 = [
        {
            "t": "La prueba de la línea horizontal, en tres casos",
            "f": "[D] diapositiva 33 · [S] p. 199",
            "c": [
                ("fig", _fig_horizontal),
                ("md",
                 "- **Izquierda:** la horizontal $y=2$ corta **dos veces** → no inyectiva. "
                 "Además ninguna horizontal por debajo del vértice corta → tampoco suprayectiva sobre $\\mathbb{R}$.\n"
                 "- **Centro:** toda horizontal corta a lo sumo una vez → inyectiva. Pero las "
                 "horizontales con $y\\le -2$ no cortan → no suprayectiva sobre $\\mathbb{R}$.\n"
                 "- **Derecha:** toda horizontal corta exactamente una vez → biyectiva."),
                ("info", "La prueba es **visual y rápida**, pero no sustituye a la demostración "
                         "algebraica en un examen. Sirve para conjeturar qué se va a demostrar."),
            ],
        },
        {
            "t": "Demostrar inyectividad algebraicamente",
            "f": "[D] diapositiva 28 · [S] Ejemplo 3, p. 200",
            "c": [
                ("md", "Probar que $f(x)=3x-1$ es inyectiva."),
                ("md", "**Estructura de la demostración:** se *supone* que dos salidas son iguales y se "
                       "*deduce* que las entradas lo eran."),
                ("md", "Sean $x_1,x_2$ con $f(x_1)=f(x_2)$. Entonces:"),
                ("tex", r"3x_{1}-1=3x_{2}-1"),
                ("tex", r"3x_{1}=3x_{2} \qquad (\text{sumando } 1)"),
                ("tex", r"x_{1}=x_{2} \qquad (\text{dividiendo entre } 3)"),
                ("ok", "Como $f(x_1)=f(x_2)$ obliga a $x_1=x_2$, la función es inyectiva."),
                ("err", "Error frecuente: escribir «como $x_1\\neq x_2$ entonces $3x_1-1\\neq3x_2-1$» y "
                        "quedarse ahí. Eso es la definición, no una demostración. El camino limpio es "
                        "el contrapositivo de arriba."),
            ],
        },
        {
            "t": "Demostrar suprayectividad construyendo la preimagen",
            "f": "[D] diapositiva 30",
            "c": [
                ("md", "Probar que $f\\colon\\mathbb{R}\\to\\mathbb{R}$, $f(x)=2x+5$, es suprayectiva."),
                ("md", "**Estructura:** se toma un $y$ **arbitrario** del codominio y se **exhibe** un "
                       "$x$ del dominio que lo produce."),
                ("md", "Sea $y\\in\\mathbb{R}$ cualquiera. Se busca $x$ con $2x+5=y$. Despejando:"),
                ("tex", r"2x=y-5 \qquad\Longrightarrow\qquad x=\frac{y-5}{2}"),
                ("md", "**Dos verificaciones obligatorias:**"),
                ("md", "1. *¿Ese $x$ está en el dominio?* Sí: $\\tfrac{y-5}{2}$ es un real para "
                       "cualquier real $y$.\n"
                       "2. *¿Realmente da $y$?* Se comprueba:"),
                ("tex", r"f\!\left(\frac{y-5}{2}\right)=2\cdot\frac{y-5}{2}+5=(y-5)+5=y \ \checkmark"),
                ("ok", "Todo $y\\in\\mathbb{R}$ tiene preimagen, así que $f$ es suprayectiva."),
                ("warn", "Contraste: para $g(x)=x^{2}$ con codominio $\\mathbb{R}$, el despeje "
                         "$x=\\pm\\sqrt{y}$ **falla** para $y<0$. Basta $y=-1$ como contraejemplo: "
                         "$x^2=-1$ no tiene solución real."),
            ],
        },
        {
            "t": "Combinaciones de funciones y sus dominios",
            "f": "[S] Ejemplo 1, p. 191",
            "c": [
                ("md", "Sean $f(x)=\\dfrac{1}{x-2}$ y $g(x)=\\sqrt{x}$. Hallar $f+g$, $f-g$, $fg$ y "
                       "$f/g$ con sus dominios, y evaluarlas en $x=4$."),
                ("md", "**Paso 0. Dominios individuales.** Es siempre lo primero:"),
                ("tex", r"\operatorname{Dom}(f)=\{x : x\neq 2\}, \qquad \operatorname{Dom}(g)=\{x : x\ge 0\}"),
                ("md", "**Paso 1. Intersección.** Hay que cumplir **las dos** condiciones a la vez:"),
                ("tex", r"A\cap B=\{x : x\ge 0 \ \text{y}\ x\neq 2\}=[0,2)\cup(2,+\infty)"),
                ("md", "**Paso 2. Las cuatro combinaciones.** Las tres primeras heredan $A\\cap B$ tal cual:"),
                ("tex", r"(f+g)(x)=\frac{1}{x-2}+\sqrt{x}, \qquad \operatorname{Dom}=[0,2)\cup(2,+\infty)"),
                ("tex", r"(f-g)(x)=\frac{1}{x-2}-\sqrt{x}, \qquad \operatorname{Dom}=[0,2)\cup(2,+\infty)"),
                ("tex", r"(fg)(x)=\frac{\sqrt{x}}{x-2}, \qquad \operatorname{Dom}=[0,2)\cup(2,+\infty)"),
                ("md", "**El cociente pide una exclusión extra:** los ceros de $g$. Como "
                       "$\\sqrt{x}=0\\iff x=0$, hay que sacar el $0$:"),
                ("tex", r"\left(\frac{f}{g}\right)(x)=\frac{1/(x-2)}{\sqrt{x}}=\frac{1}{(x-2)\sqrt{x}}, \qquad \operatorname{Dom}=(0,2)\cup(2,+\infty)"),
                ("md", "**Paso 3. Evaluación en $x=4$.** Está en todos los dominios, así que los cuatro "
                       "valores existen. Con $f(4)=\\tfrac12$ y $g(4)=2$:"),
                ("tex", r"(f+g)(4)=\tfrac{1}{2}+2=\tfrac{5}{2}, \qquad (f-g)(4)=\tfrac{1}{2}-2=-\tfrac{3}{2}"),
                ("tex", r"(fg)(4)=\tfrac{1}{2}\cdot 2=1, \qquad \left(\tfrac{f}{g}\right)(4)=\frac{1/2}{2}=\tfrac{1}{4}"),
                ("info", "Nótese que evaluar **primero** cada función y **después** operar es mucho más "
                         "rápido que sustituir en la fórmula combinada. Es válido justamente porque la "
                         "definición es puntual: $(f+g)(x)=f(x)+g(x)$."),
            ],
        },
    ]
    mostrar_ejemplos(ejemplos_u3)

    st.markdown("---")
    st.subheader("Ejercicios")

    def _fig_x2_tres_casos():
        fig, axes = plt.subplots(1, 3, figsize=(9.5, 2.9))
        xf = np.linspace(-2.3, 2.3, 400)
        xp = np.linspace(0, 2.3, 300)
        axes[0].plot(xf, xf ** 2, color=AZUL, lw=2)
        axes[0].axhline(2, color=ROJO, ls="--")
        axes[0].axhline(-1, color=ROJO, ls="--")
        axes[0].plot([-np.sqrt(2), np.sqrt(2)], [2, 2], "o", color=ROJO, ms=6)
        axes[0].set_title(r"$g:\mathbb{R}\to\mathbb{R}$" "\nni iny. ni supra.", fontsize=8.5)
        axes[1].plot(xf, xf ** 2, color=AZUL, lw=2)
        axes[1].axhline(2, color=OCRE, ls="--")
        axes[1].plot([-np.sqrt(2), np.sqrt(2)], [2, 2], "o", color=OCRE, ms=6)
        axes[1].axhspan(-1.2, 0, color="0.85")
        axes[1].set_title(r"$h:\mathbb{R}\to[0,\infty)$" "\nsupra., no iny.", fontsize=8.5)
        axes[2].plot(xp, xp ** 2, color=VERDE, lw=2)
        axes[2].axhline(2, color=OCRE, ls="--")
        axes[2].plot([np.sqrt(2)], [2], "o", color=VERDE, ms=7)
        axes[2].set_title(r"$p:[0,\infty)\to[0,\infty)$" "\nbiyectiva", fontsize=8.5)
        for a in axes:
            a.axhline(0, color="0.3", lw=0.8)
            a.axvline(0, color="0.3", lw=0.8)
            a.grid(alpha=0.2, ls=":")
            a.set_ylim(-1.2, 5)
        fig.tight_layout()
        return fig

    def _fig_restriccion():
        fig, axes = plt.subplots(1, 2, figsize=(7.8, 3.0))
        x = np.linspace(-2.6, 2.6, 400)
        xr = np.linspace(0, 2.6, 300)
        axes[0].plot(x, 4 - x ** 2, color=AZUL, lw=2)
        axes[0].axhline(3, color=ROJO, ls="--")
        axes[0].plot([-1, 1], [3, 3], "o", color=ROJO, ms=6)
        axes[0].set_title(r"$f(x)=4-x^{2}$ en $\mathbb{R}$: dos cortes", fontsize=8.5, color=ROJO)
        axes[1].plot(x, 4 - x ** 2, color="0.8", lw=1.4, ls="--")
        axes[1].plot(xr, 4 - xr ** 2, color=VERDE, lw=2.4)
        axes[1].axhline(3, color=OCRE, ls="--")
        axes[1].plot([1], [3], "o", color=VERDE, ms=7)
        axes[1].set_title(r"restringida a $x\geq 0$: un corte", fontsize=8.5, color=VERDE)
        for a in axes:
            a.axhline(0, color="0.3", lw=0.8)
            a.axvline(0, color="0.3", lw=0.8)
            a.grid(alpha=0.2, ls=":")
            a.set_ylim(-3, 5)
        fig.tight_layout()
        return fig

    def _fig_suma_grafica():
        fig, ax = nueva_fig(figsize=(5.8, 3.6))
        x = np.linspace(0, 5, 300)
        ax.plot(x, x - 2, color="0.55", lw=1.6, ls="--", label=r"$f(x)=x-2$")
        ax.plot(x, np.sqrt(x), color=OCRE, lw=1.6, ls="--", label=r"$g(x)=\sqrt{x}$")
        ax.plot(x, x - 2 + np.sqrt(x), color=AZUL, lw=2.4, label=r"$(f+g)(x)$")
        ax.plot([0], [-2], "o", color=AZUL, ms=7)
        ax.plot([2], [np.sqrt(2)], "o", color=AZUL, ms=7)
        ax.plot([1], [0], "o", color=VERDE, ms=7)
        ax.annotate(r"$g=0$: aquí $f+g$ toca a $f$", (0, -2), textcoords="offset points",
                    xytext=(10, -4), fontsize=7.5)
        ax.annotate(r"$f=0$: aquí $f+g$ toca a $g$", (2, np.sqrt(2)), textcoords="offset points",
                    xytext=(6, -22), fontsize=7.5)
        ax.annotate(r"$x=1$", (1, 0), textcoords="offset points", xytext=(-4, 10),
                    fontsize=7.5, color=VERDE)
        ax.set_xlim(-0.4, 5.2)
        ax.set_ylim(-2.8, 5.5)
        ax.legend(fontsize=8, loc="upper left")
        fig.tight_layout()
        return fig

    def _fig_transformacion():
        fig, ax = nueva_fig(figsize=(5.6, 3.6))
        x = np.linspace(-2, 4, 400)
        ax.plot(x, x ** 2, color="0.6", lw=1.6, ls="--", label=r"$f(x)=x^{2}$")
        ax.plot(x, (x - 1) ** 2, color=OCRE, lw=1.6, label=r"$f(x-1)$")
        ax.plot(x, -2 * (x - 1) ** 2 + 3, color=AZUL, lw=2.2, label=r"$-2f(x-1)+3$")
        ax.plot([1], [3], "o", color=AZUL, ms=7)
        ax.set_ylim(-6, 8)
        ax.legend(fontsize=8, loc="lower center")
        ax.set_title("Cadena de transformaciones", fontsize=10)
        fig.tight_layout()
        return fig

    def _fig_valor_absoluto():
        fig, ax = nueva_fig(figsize=(5.2, 3.4))
        x = np.linspace(-3.2, 3.2, 400)
        ax.plot(x, x ** 2 - 4, color="0.6", lw=1.6, ls="--", label=r"$f(x)=x^{2}-4$")
        ax.plot(x, np.abs(x ** 2 - 4), color=AZUL, lw=2.2, label=r"$g(x)=|x^{2}-4|$")
        ax.plot([-2, 2], [0, 0], "o", color=VERDE, ms=7)
        ax.plot([0], [4], "o", color=AZUL, ms=6)
        ax.plot([0], [-4], "o", mfc="white", mec="0.6", ms=6)
        ax.set_ylim(-5.5, 6.5)
        ax.legend(fontsize=8, loc="upper center")
        fig.tight_layout()
        return fig

    def _fig_horizontales():
        fig, ax = nueva_fig(figsize=(6.0, 3.0))
        t = np.linspace(0, np.pi, 300)
        xs = 1 + np.cos(t)
        ys = np.sin(t)
        ax.plot(xs, ys, color="0.55", lw=1.8, ls="--", label=r"$y=f(x)$,  $[0,2]$")
        ax.plot(xs / 2, ys, color=AZUL, lw=2.2, label=r"$y=f(2x)$,  $[0,1]$")
        ax.plot(xs * 2, ys, color=OCRE, lw=2.2, label=r"$y=f(\frac{1}{2}x)$,  $[0,4]$")
        ax.set_xlim(-0.4, 4.4)
        ax.set_ylim(-0.25, 1.7)
        ax.legend(fontsize=7.5, loc="upper right")
        ax.set_title(r"$f(x)=\sqrt{2x-x^{2}}$ y sus transformaciones horizontales", fontsize=9)
        fig.tight_layout()
        return fig

    ejercicios_u3 = [
        {
            "t": "Clasificar una función lineal",
            "f": "[D] diapositiva 34 (Ejercicio 4 de la unidad)",
            "e": [("md", "Sea $f\\colon\\mathbb{R}\\to\\mathbb{R}$, $f(x)=3x-2$. Determinar si es "
                         "inyectiva, suprayectiva y/o biyectiva.")],
            "s": [
                ("md", "**Inyectividad.** Supóngase $f(x_1)=f(x_2)$:"),
                ("tex", r"3x_{1}-2=3x_{2}-2 \;\Longrightarrow\; 3x_{1}=3x_{2} \;\Longrightarrow\; x_{1}=x_{2}\ \checkmark"),
                ("md", "**Suprayectividad.** Sea $y\\in\\mathbb{R}$ arbitrario; se busca $x$ con $3x-2=y$:"),
                ("tex", r"3x=y+2 \;\Longrightarrow\; x=\frac{y+2}{3}\in\mathbb{R}\ \checkmark"),
                ("md", "Verificación: $f\\!\\left(\\tfrac{y+2}{3}\\right)=3\\cdot\\tfrac{y+2}{3}-2=y+2-2=y$."),
                ("ok", "$f$ es **biyectiva**, y por tanto tiene inversa: "
                       "$f^{-1}(x)=\\dfrac{x+2}{3}$."),
                ("info", "La generalización a $f(x)=mx+b$ es el ejercicio 4 de esta misma pestaña."),
            ],
        },
        {
            "t": "La misma fórmula, tres funciones distintas",
            "f": "[D] diapositivas 35–37 (Ejercicios 5, 6 y 7 de la unidad)",
            "e": [("md", "Clasificar cada una:\n\n"
                         "(a) $g\\colon\\mathbb{R}\\to\\mathbb{R}$, $g(x)=x^{2}$  \n"
                         "(b) $h\\colon\\mathbb{R}\\to[0,+\\infty)$, $h(x)=x^{2}$  \n"
                         "(c) $p\\colon[0,+\\infty)\\to[0,+\\infty)$, $p(x)=x^{2}$")],
            "s": [
                ("md", "**(a) $g\\colon\\mathbb{R}\\to\\mathbb{R}$**"),
                ("md", "*Inyectiva?* Contraejemplo: $g(2)=4=g(-2)$ pero $2\\neq-2$. **No.**"),
                ("md", "*Suprayectiva?* Tómese $y=-1\\in\\mathbb{R}$. La ecuación $x^{2}=-1$ no tiene "
                       "solución real. **No.** En efecto "
                       "$\\operatorname{Ran}(g)=[0,\\infty)\\subsetneq\\mathbb{R}$."),
                ("err", "$g$ no es ni inyectiva ni suprayectiva."),
                ("md", "**(b) $h\\colon\\mathbb{R}\\to[0,+\\infty)$** — se cambió sólo el codominio."),
                ("md", "*Inyectiva?* El mismo contraejemplo sigue funcionando: $h(3)=9=h(-3)$. **No.**"),
                ("md", "*Suprayectiva?* Sea $y\\ge0$. Se propone $x=\\sqrt{y}$, que es real porque "
                       "$y\\ge0$, y $h(\\sqrt y)=(\\sqrt y)^{2}=y$. **Sí.**"),
                ("warn", "$h$ es suprayectiva pero no inyectiva. **Cambiar el codominio arregló la "
                         "suprayectividad**, pero la inyectividad depende del dominio, así que no cambió."),
                ("md", "**(c) $p\\colon[0,+\\infty)\\to[0,+\\infty)$** — ahora se restringió también el dominio."),
                ("md", "*Inyectiva?* Sean $x_1,x_2\\ge0$ con $x_1^{2}=x_2^{2}$:"),
                ("tex", r"x_{1}^{2}-x_{2}^{2}=0 \;\Longrightarrow\; (x_{1}-x_{2})(x_{1}+x_{2})=0"),
                ("md", "Como $x_1,x_2\\ge0$: si $x_1+x_2>0$, el otro factor debe anularse y "
                       "$x_1=x_2$. Si $x_1+x_2=0$, al ser ambos no negativos, $x_1=x_2=0$. En todo "
                       "caso $x_1=x_2$. **Sí.**"),
                ("md", "*Suprayectiva?* Sea $y\\ge0$: $x=\\sqrt y\\ge0$ está en el dominio y "
                       "$p(\\sqrt y)=y$. **Sí.**"),
                ("ok", "$p$ es **biyectiva**, y su inversa es $p^{-1}(x)=\\sqrt{x}$."),
                ("fig", _fig_x2_tres_casos),
                ("info", "**Éste es el ejercicio clave de la sección.** La fórmula no determina las "
                         "propiedades; la terna (fórmula, dominio, codominio) sí. Restringir el "
                         "**dominio** arregla la inyectividad; ajustar el **codominio** arregla la "
                         "suprayectividad. Es exactamente lo que hace Stewart en la p. 200 al pasar "
                         "de $g(x)=x^2$ a $h(x)=x^{2}$ con $x\\ge0$."),
            ],
        },
        {
            "t": "Batería: ¿uno a uno? ¿y sobre el codominio declarado?",
            "f": "[S] Ejercicios 11, 13, 15, 17, 18 y 19, p. 205 (con codominio declarado)",
            "e": [("md", "Para cada función, decidir si es inyectiva, suprayectiva y biyectiva:\n\n"
                         "(a) $f\\colon\\mathbb{R}\\to\\mathbb{R}$, $f(x)=-2x+4$  \n"
                         "(b) $g\\colon[0,+\\infty)\\to[0,+\\infty)$, $g(x)=\\sqrt{x}$  \n"
                         "(c) $h\\colon\\mathbb{R}\\to\\mathbb{R}$, $h(x)=x^{2}-2x$  \n"
                         "(d) $F\\colon\\mathbb{R}\\to\\mathbb{R}$, $F(x)=x^{4}+5$  \n"
                         "(e) $G\\colon[0,2]\\to[5,21]$, $G(x)=x^{4}+5$  \n"
                         "(f) $K\\colon\\mathbb{R}\\setminus\\{0\\}\\to\\mathbb{R}$, $K(x)=\\dfrac{1}{x^{2}}$")],
            "s": [
                ("md", "**(a)** *Iny.:* $-2x_1+4=-2x_2+4\\Rightarrow-2x_1=-2x_2\\Rightarrow x_1=x_2$ ✓. "
                       "*Supra.:* dado $y$, se despeja"),
                ("tex", r"-2x=y-4 \;\Longrightarrow\; x=\frac{4-y}{2}\in\mathbb{R}, \qquad f\!\left(\tfrac{4-y}{2}\right)=-(4-y)+4=y\ \checkmark"),
                ("ok", "(a) es **biyectiva**."),
                ("md", "**(b)** *Iny.:* si $\\sqrt{x_1}=\\sqrt{x_2}$, elevando al cuadrado $x_1=x_2$ ✓. "
                       "*Supra.:* dado $y\\ge0$, se toma $x=y^{2}\\ge0$, que está en el dominio, y"),
                ("tex", r"g(y^{2})=\sqrt{y^{2}}=|y|=y \quad (\text{pues } y\ge 0)\ \checkmark"),
                ("ok", "(b) es **biyectiva**. Coherente con el libro: la raíz es creciente, y toda "
                       "función creciente es uno a uno."),
                ("md", "**(c)** Conviene completar el cuadrado antes de opinar:"),
                ("tex", r"h(x)=x^{2}-2x=(x-1)^{2}-1"),
                ("md", "*Iny.:* la parábola es simétrica respecto de $x=1$, así que hay pares. "
                       "Contraejemplo: $h(0)=0$ y $h(2)=4-4=0$. **No.** "
                       "*Supra.:* $(x-1)^{2}\\ge0\\Rightarrow h(x)\\ge-1$, así que $y=-2$ no tiene "
                       "preimagen. **No.**"),
                ("err", "(c) no es ninguna de las tres. Su rango es $[-1,+\\infty)$."),
                ("md", "**(d)** *Iny.:* $F(1)=6=F(-1)$. **No** (potencia par). "
                       "*Supra.:* $x^{4}\\ge0\\Rightarrow F(x)\\ge5$, así que $y=0$ no tiene preimagen. **No.**"),
                ("md", "**(e)** La *misma fórmula* que (d), pero con dominio y codominio recortados."),
                ("md", "*Iny.:* sean $x_1,x_2\\in[0,2]$ con $x_1^{4}+5=x_2^{4}+5$. Entonces "
                       "$x_1^{4}=x_2^{4}$, de donde $|x_1|=|x_2|$, y como ambos son $\\ge0$, "
                       "$x_1=x_2$ ✓."),
                ("md", "*Supra.:* sea $y\\in[5,21]$. Se propone $x=\\sqrt[4]{y-5}$. Verificaciones:"),
                ("tex", r"5\le y\le 21 \;\Longrightarrow\; 0\le y-5\le 16 \;\Longrightarrow\; 0\le \sqrt[4]{y-5}\le 2"),
                ("md", "así que $x\\in[0,2]$ ✓, y $G(x)=\\left(\\sqrt[4]{y-5}\\right)^{4}+5=y$ ✓."),
                ("ok", "(e) es **biyectiva**. Los extremos del codominio no son un capricho: "
                       "$G(0)=5$ y $G(2)=16+5=21$."),
                ("md", "**(f)** *Iny.:* $K(1)=1=K(-1)$. **No.** "
                       "*Supra.:* $\\dfrac{1}{x^{2}}>0$ siempre, así que ningún $y\\le0$ tiene preimagen. **No.** "
                       "Su rango es $(0,+\\infty)$."),
                ("info", "Compárense (d) y (e): **misma regla, distinta función.** Recortar el dominio "
                         "a $[0,2]$ mató los pares $\\pm x$ (inyectividad) y declarar el codominio "
                         "$[5,21]$ igual al rango dio la suprayectividad."),
            ],
        },
        {
            "t": "¿Cuándo una función lineal tiene inversa?",
            "f": "[S] Ejercicio 90, p. 206",
            "e": [("md", "Sea $f\\colon\\mathbb{R}\\to\\mathbb{R}$, $f(x)=mx+b$.\n\n"
                         "(a) ¿Qué debe cumplir la pendiente $m$ para que $f$ sea uno a uno?  \n"
                         "(b) Con esa condición, ¿es biyectiva?  \n"
                         "(c) Hallar $f^{-1}$. ¿Es lineal? ¿Cuál es su pendiente?")],
            "s": [
                ("md", "**(a)** Hay que separar dos casos, y el caso $m=0$ es el interesante."),
                ("md", "*Caso $m\\neq0$.* Supóngase $f(x_1)=f(x_2)$:"),
                ("tex", r"mx_{1}+b=mx_{2}+b \;\Longrightarrow\; mx_{1}=mx_{2} \;\Longrightarrow\; x_{1}=x_{2}"),
                ("warn", "El último paso es dividir entre $m$, y **sólo es válido si $m\\neq0$**. Ahí "
                         "es donde entra la hipótesis; no es un detalle."),
                ("md", "*Caso $m=0$.* Entonces $f(x)=b$ es constante: $f(0)=f(1)=b$ con $0\\neq1$. "
                       "**No** es uno a uno (y su rango es $\\{b\\}$, así que tampoco es suprayectiva)."),
                ("ok", "$f$ es uno a uno **si y sólo si** $m\\neq0$."),
                ("md", "**(b)** Sea $y\\in\\mathbb{R}$ y $m\\neq0$. Despejando:"),
                ("tex", r"mx=y-b \;\Longrightarrow\; x=\frac{y-b}{m}\in\mathbb{R}"),
                ("tex", r"f\!\left(\frac{y-b}{m}\right)=m\cdot\frac{y-b}{m}+b=(y-b)+b=y\ \checkmark"),
                ("ok", "Suprayectiva; con (a), **biyectiva** para todo $m\\neq0$."),
                ("md", "**(c)** Intercambiando nombres:"),
                ("tex", r"f^{-1}(x)=\frac{x-b}{m}=\frac{1}{m}\,x-\frac{b}{m}"),
                ("md", "Es de la forma $Mx+B$ con $M=\\dfrac{1}{m}$ y $B=-\\dfrac{b}{m}$: **sí es "
                       "lineal**, y su pendiente es el **recíproco** de la de $f$."),
                ("info", "Coherencia geométrica: reflejar una recta en $y=x$ intercambia los papeles "
                         "de $\\Delta x$ y $\\Delta y$, y una pendiente $m=\\tfrac{\\Delta y}{\\Delta x}$ "
                         "se vuelve $\\tfrac{\\Delta x}{\\Delta y}=\\tfrac1m$. Verificación con el "
                         "ejercicio 1: $f(x)=3x-2$ tiene $m=3$ y "
                         "$f^{-1}(x)=\\tfrac{x+2}{3}$ tiene pendiente $\\tfrac13$ ✓."),
                ("md", "Caso especial: si $m=1$ y $b=0$, $f=f^{-1}=\\mathrm{Id}$."),
            ],
        },
        {
            "t": "Restringir el dominio para lograr biyectividad",
            "f": "[S] Ejercicios 75, 76, 77 y 78, p. 206",
            "e": [("md", "Ninguna de estas funciones es uno a uno en su dominio natural. Restringir el "
                         "dominio para que lo sea, declarar el codominio que la vuelve biyectiva y "
                         "hallar la inversa correspondiente:\n\n"
                         "(a) $f(x)=4-x^{2}$  (b) $g(x)=(x-1)^{2}$  "
                         "(c) $h(x)=(x+2)^{2}$  (d) $k(x)=|x-3|$")],
            "s": [
                ("warn", "El libro advierte que **hay más de una respuesta correcta**: la restricción "
                         "no es única. Lo que sí es obligatorio es *declararla* y ser consistente con "
                         "ella al elegir el signo de la raíz."),
                ("md", "**Estrategia común:** todas son simétricas respecto de una recta vertical "
                       "(el vértice o el pico). Se corta ahí y se conserva una de las dos mitades."),
                ("md", "**(a)** $f(x)=4-x^{2}$ tiene vértice en $x=0$; no es uno a uno porque "
                       "$f(1)=3=f(-1)$. Se toma la mitad derecha:"),
                ("tex", r"f\colon[0,+\infty)\to(-\infty,4]"),
                ("md", "*Iny.:* si $x_1,x_2\\ge0$ y $4-x_1^{2}=4-x_2^{2}$, entonces $x_1^{2}=x_2^{2}$ "
                       "y al ser ambos no negativos $x_1=x_2$ ✓.  \n"
                       "*Rango:* $x\\ge0\\Rightarrow x^{2}\\ge0\\Rightarrow f(x)\\le4$, y todo $y\\le4$ "
                       "se alcanza con $x=\\sqrt{4-y}\\ge0$ ✓."),
                ("tex", r"y=4-x^{2} \;\Longrightarrow\; x^{2}=4-y \;\Longrightarrow\; x=+\sqrt{4-y}"),
                ("tex", r"f^{-1}(x)=\sqrt{4-x}, \qquad \operatorname{Dom}(f^{-1})=(-\infty,4]"),
                ("fig", _fig_restriccion),
                ("md", "**(b)** $g(x)=(x-1)^{2}$: el vértice está en $x=1$. Se restringe a $x\\ge1$:"),
                ("tex", r"g\colon[1,+\infty)\to[0,+\infty), \qquad y=(x-1)^{2} \Longrightarrow x-1=+\sqrt{y}"),
                ("tex", r"g^{-1}(x)=1+\sqrt{x}, \qquad \operatorname{Dom}(g^{-1})=[0,+\infty)"),
                ("md", "**(c)** $h(x)=(x+2)^{2}$: vértice en $x=-2$. Se restringe a $x\\ge-2$:"),
                ("tex", r"h\colon[-2,+\infty)\to[0,+\infty), \qquad h^{-1}(x)=-2+\sqrt{x}"),
                ("md", "**(d)** $k(x)=|x-3|$: el pico está en $x=3$. Para $x\\ge3$ el valor absoluto "
                       "se quita sin cambiar signo, $k(x)=x-3$:"),
                ("tex", r"k\colon[3,+\infty)\to[0,+\infty), \qquad y=x-3 \Longrightarrow k^{-1}(x)=x+3"),
                ("md", "**Verificación en un punto (b):** $g(4)=9$ y $g^{-1}(9)=1+3=4$ ✓."),
                ("err", "El error clásico es escribir $f^{-1}(x)=\\pm\\sqrt{4-x}$. Una función **no** "
                        "puede devolver dos valores: el signo lo fija la restricción que uno mismo "
                        "eligió. Si en (a) se hubiera tomado $x\\le0$, la respuesta correcta sería "
                        "$f^{-1}(x)=-\\sqrt{4-x}$."),
                ("info", "Este procedimiento es exactamente el que define $\\arcsin$, $\\arccos$ y "
                         "$\\arctan$: el seno no es inyectivo en $\\mathbb{R}$, así que se le recorta "
                         "el dominio a $\\left[-\\tfrac{\\pi}{2},\\tfrac{\\pi}{2}\\right]$."),
            ],
        },
        {
            "t": "Función racional: biyectividad y preimagen",
            "f": "estilo [S] §2.7",
            "e": [("md", "Sea $f\\colon\\mathbb{R}\\setminus\\{-1\\}\\to\\mathbb{R}\\setminus\\{1\\}$ "
                         "definida por $f(x)=\\dfrac{x}{x+1}$. Probar que es biyectiva.")],
            "s": [
                ("md", "**Inyectividad.** Sea $f(x_1)=f(x_2)$, con $x_1,x_2\\neq-1$:"),
                ("tex", r"\frac{x_{1}}{x_{1}+1}=\frac{x_{2}}{x_{2}+1}"),
                ("md", "Multiplicación cruzada (válida, los denominadores no son cero):"),
                ("tex", r"x_{1}(x_{2}+1)=x_{2}(x_{1}+1)"),
                ("tex", r"x_{1}x_{2}+x_{1}=x_{1}x_{2}+x_{2} \;\Longrightarrow\; x_{1}=x_{2}\ \checkmark"),
                ("md", "**Suprayectividad.** Sea $y\\neq 1$. Se resuelve $\\dfrac{x}{x+1}=y$:"),
                ("tex", r"x=y(x+1)=yx+y \;\Longrightarrow\; x-yx=y \;\Longrightarrow\; x(1-y)=y"),
                ("tex", r"x=\frac{y}{1-y}"),
                ("md", "**Verificación 1:** el despeje requiere $1-y\\neq0$, y justamente $y\\neq1$ "
                       "por hipótesis. Por eso se excluyó el $1$ del codominio."),
                ("md", "**Verificación 2:** ¿ese $x$ está en el dominio, es decir $x\\neq-1$? "
                       "Si $\\tfrac{y}{1-y}=-1$ entonces $y=-(1-y)=y-1$, o sea $0=-1$, absurdo. "
                       "Luego $x\\neq-1$ siempre. ✓"),
                ("ok", "$f$ es biyectiva y $f^{-1}(y)=\\dfrac{y}{1-y}$."),
                ("info", "El valor $y=1$ excluido del codominio es la **asíntota horizontal** de la "
                         "gráfica: se acerca pero nunca se alcanza. Excluir la asíntota es la manera "
                         "estándar de volver suprayectiva una función racional."),
            ],
        },
        {
            "t": "Biyectividad de funciones irracionales (y una involución de verdad)",
            "f": "[S] Ejercicios 51 y 58, p. 205 · [S] Ejercicio 34, p. 205",
            "e": [("md", "(a) Sea $f(x)=\\sqrt{2+5x}$. Determinar su dominio natural, declarar el "
                         "codominio que la hace biyectiva y hallar $f^{-1}$.  \n"
                         "(b) Sea $q(x)=\\sqrt{9-x^{2}}$ con $0\\le x\\le 3$ y codominio $[0,3]$. "
                         "Probar que es biyectiva y hallar $q^{-1}$. ¿Qué tiene de especial el resultado?")],
            "s": [
                ("md", "**(a) Dominio.** Radicando de índice par $\\ge0$:"),
                ("tex", r"2+5x\ge 0 \iff x\ge -\tfrac{2}{5} \qquad\Longrightarrow\qquad \operatorname{Dom}(f)=\left[-\tfrac{2}{5},+\infty\right)"),
                ("md", "*Inyectividad.* Si $\\sqrt{2+5x_1}=\\sqrt{2+5x_2}$, elevando al cuadrado "
                       "(legal: ambos lados son $\\ge0$):"),
                ("tex", r"2+5x_{1}=2+5x_{2} \;\Longrightarrow\; x_{1}=x_{2}\ \checkmark"),
                ("md", "*Rango y suprayectividad.* La raíz principal es $\\ge0$, así que "
                       "$\\operatorname{Ran}(f)\\subseteq[0,\\infty)$. Recíprocamente, dado $y\\ge0$ "
                       "se resuelve $\\sqrt{2+5x}=y$:"),
                ("tex", r"2+5x=y^{2} \;\Longrightarrow\; x=\frac{y^{2}-2}{5}"),
                ("md", "¿Está ese $x$ en el dominio? Hay que comprobarlo, no suponerlo:"),
                ("tex", r"\frac{y^{2}-2}{5}\ \ge\ -\frac{2}{5} \iff y^{2}-2\ge -2 \iff y^{2}\ge 0\ \checkmark"),
                ("ok", "$f\\colon\\left[-\\tfrac25,\\infty\\right)\\to[0,\\infty)$ es **biyectiva**, "
                       "con $f^{-1}(x)=\\dfrac{x^{2}-2}{5}$, $\\operatorname{Dom}(f^{-1})=[0,+\\infty)$."),
                ("warn", "El dominio de $f^{-1}$ **no** es $\\mathbb{R}$ aunque la fórmula "
                         "$\\tfrac{x^{2}-2}{5}$ sea un polinomio. Se hereda del rango de $f$."),
                ("md", "**(b)** *Inyectividad.* Sean $x_1,x_2\\in[0,3]$ con $\\sqrt{9-x_1^{2}}=\\sqrt{9-x_2^{2}}$:"),
                ("tex", r"9-x_{1}^{2}=9-x_{2}^{2} \;\Longrightarrow\; x_{1}^{2}=x_{2}^{2} \;\Longrightarrow\; x_{1}=x_{2}"),
                ("md", "(la última implicación usa que **ambos son $\\ge0$**; sin la restricción "
                       "$x\\ge0$ sería falsa)."),
                ("md", "*Suprayectividad sobre $[0,3]$.* Sea $y\\in[0,3]$ y propóngase "
                       "$x=\\sqrt{9-y^{2}}$. Verificaciones:"),
                ("tex", r"0\le y\le 3 \;\Longrightarrow\; 0\le 9-y^{2}\le 9 \;\Longrightarrow\; 0\le x\le 3\ \checkmark"),
                ("tex", r"q(x)=\sqrt{9-\left(\sqrt{9-y^{2}}\right)^{2}}=\sqrt{9-(9-y^{2})}=\sqrt{y^{2}}=y\ \checkmark"),
                ("ok", "$q$ es **biyectiva** y $q^{-1}(x)=\\sqrt{9-x^{2}}=q(x)$: **es su propia "
                       "inversa** (una *involución*)."),
                ("info", "Geométricamente es el cuarto de circunferencia $x^{2}+y^{2}=9$ en el primer "
                         "cuadrante, que es simétrico respecto de la recta $y=x$; reflejarlo en $y=x$ "
                         "lo deja igual. Éste **sí** es un ejemplo legítimo de involución, a "
                         "diferencia de la afirmación falsa de la diapositiva 60(b) (ver pestaña 4 y "
                         "pestaña de errores)."),
            ],
        },
        {
            "t": "Refutar inyectividad con un contraejemplo",
            "f": "estilo [S] §2.7 · cf. Ejercicio 65, p. 205",
            "e": [("md", "Sea $f\\colon\\mathbb{R}\\to\\mathbb{R}$, $f(x)=x^{3}-3x$. "
                         "¿Es inyectiva? ¿Suprayectiva?")],
            "s": [
                ("md", "**Inyectividad.** Como es un polinomio impar de grado 3, la línea horizontal "
                       "sugiere que hay cortes múltiples. Se busca el contraejemplo resolviendo $f(x)=0$:"),
                ("tex", r"x^{3}-3x=x(x^{2}-3)=0 \;\Longrightarrow\; x=0,\ x=\sqrt{3},\ x=-\sqrt{3}"),
                ("md", "Tres entradas distintas con la misma salida:"),
                ("tex", r"f(0)=f(\sqrt{3})=f(-\sqrt{3})=0"),
                ("err", "**No es inyectiva.** Con exhibir **un solo** par $x_1\\neq x_2$ tal que "
                        "$f(x_1)=f(x_2)$ basta; no hace falta más."),
                ("md", "**Suprayectividad.** Sí lo es. Argumento: $f$ es un polinomio (continuo) con"),
                ("tex", r"\lim_{x\to+\infty}f(x)=+\infty, \qquad \lim_{x\to-\infty}f(x)=-\infty"),
                ("md", "Por el Teorema del Valor Intermedio, toma todos los valores intermedios, es "
                       "decir todo $\\mathbb{R}$. Formalmente: para cualquier $y$, la ecuación "
                       "$x^{3}-3x-y=0$ es cúbica y toda cúbica real tiene al menos una raíz real."),
                ("ok", "Suprayectiva pero no inyectiva; por lo tanto **no** biyectiva y **no** tiene "
                       "inversa global."),
                ("info", "Contraste con $x^{3}$ (sin el $-3x$), que sí es biyectiva ([S] Ejemplo 1, "
                         "p. 200). El término lineal crea los dos «dobleces» que rompen la inyectividad."),
            ],
        },
        {
            "t": "Igualdad de funciones",
            "f": "[D] diapositiva 38",
            "e": [("md", "Decidir si son iguales:\n\n"
                         "(a) $f(x)=\\dfrac{x^{2}-1}{x-1}$ y $g(x)=x+1$  \n"
                         "(b) $p(x)=(x+1)^{2}-1$ y $q(x)=x^{2}+2x$")],
            "s": [
                ("md", "**Recordar la definición:** $f=g$ exige **dominio igual** *y* valores iguales. "
                       "El dominio se revisa **primero**."),
                ("md", "**(a)** Dominios:"),
                ("tex", r"\operatorname{Dom}(f)=\mathbb{R}\setminus\{1\}, \qquad \operatorname{Dom}(g)=\mathbb{R}"),
                ("err", "$f\\neq g$: los dominios difieren. $g(1)=2$ existe, pero $f(1)$ no."),
                ("md", "Sí es cierto que **coinciden en valores** donde ambas existen: para $x\\neq1$,"),
                ("tex", r"f(x)=\frac{(x-1)(x+1)}{x-1}=x+1=g(x)"),
                ("md", "Pero coincidir en valores no basta; hace falta el mismo dominio."),
                ("md", "**(b)** Dominios: los dos son $\\mathbb{R}$ (polinomios). Ahora los valores:"),
                ("tex", r"p(x)=(x+1)^{2}-1=x^{2}+2x+1-1=x^{2}+2x=q(x)"),
                ("ok", "$p=q$. La regla puede estar escrita de formas distintas y definir la misma "
                       "función, mientras dominio e imágenes coincidan."),
                ("info", "Este contraste es la razón por la que en cálculo se dice que "
                         "$\\dfrac{x^{2}-1}{x-1}$ tiene un «hueco» en $x=1$: la simplificación es válida "
                         "sólo fuera de ese punto. Es el germen del concepto de límite."),
            ],
        },
        {
            "t": "Operaciones algebraicas y sus dominios",
            "f": "[D] diapositiva 40",
            "e": [("md", "Sean $f(x)=\\sqrt{x}$ y $g(x)=x-3$. Hallar $(f+g)(x)$, $(fg)(x)$, "
                         "$\\left(\\tfrac{f}{g}\\right)(x)$ y $\\left(\\tfrac{g}{f}\\right)(x)$, "
                         "con sus dominios.")],
            "s": [
                ("md", "**Paso 0. Dominios individuales** y su intersección:"),
                ("tex", r"\operatorname{Dom}(f)=[0,+\infty), \quad \operatorname{Dom}(g)=\mathbb{R}"),
                ("tex", r"D=\operatorname{Dom}(f)\cap\operatorname{Dom}(g)=[0,+\infty)"),
                ("md", "**Suma y producto:** heredan $D$ sin más restricciones."),
                ("tex", r"(f+g)(x)=\sqrt{x}+x-3, \qquad \operatorname{Dom}=[0,+\infty)"),
                ("tex", r"(fg)(x)=\sqrt{x}\,(x-3), \qquad \operatorname{Dom}=[0,+\infty)"),
                ("md", "**Cociente $f/g$:** hay que quitar los ceros de $g$. Como $g(x)=0\\iff x=3$:"),
                ("tex", r"\left(\frac{f}{g}\right)(x)=\frac{\sqrt{x}}{x-3}, \qquad \operatorname{Dom}=[0,3)\cup(3,+\infty)"),
                ("md", "**Cociente $g/f$:** ahora el denominador es $\\sqrt x$, que se anula en $x=0$:"),
                ("tex", r"\left(\frac{g}{f}\right)(x)=\frac{x-3}{\sqrt{x}}, \qquad \operatorname{Dom}=(0,+\infty)"),
                ("warn", "Nótese que $f/g$ y $g/f$ tienen **dominios distintos**: el $0$ está en uno "
                         "y no en el otro. El cociente no es simétrico."),
                ("info", "Regla general: el dominio de una combinación es la intersección de los "
                         "dominios, **menos** los puntos que rompen la operación nueva."),
            ],
        },
        {
            "t": "Suma, resta, producto y cociente (con radicales)",
            "f": "[S] Ejercicios 5 y 7, p. 196",
            "e": [("md", "Hallar $f+g$, $f-g$, $fg$ y $f/g$ con sus dominios:\n\n"
                         "(a) $f(x)=x-3$, $g(x)=x^{2}$  \n"
                         "(b) $f(x)=\\sqrt{4-x^{2}}$, $g(x)=\\sqrt{1+x}$")],
            "s": [
                ("md", "**(a)** Ambos son polinomios, así que "
                       "$\\operatorname{Dom}(f)=\\operatorname{Dom}(g)=\\mathbb{R}$ y "
                       "$A\\cap B=\\mathbb{R}$."),
                ("tex", r"(f+g)(x)=x-3+x^{2}=x^{2}+x-3, \qquad \operatorname{Dom}=\mathbb{R}"),
                ("tex", r"(f-g)(x)=(x-3)-x^{2}=-x^{2}+x-3, \qquad \operatorname{Dom}=\mathbb{R}"),
                ("tex", r"(fg)(x)=(x-3)x^{2}=x^{3}-3x^{2}, \qquad \operatorname{Dom}=\mathbb{R}"),
                ("md", "Para el cociente se excluyen los ceros de $g$, es decir $x=0$ (doble, pero "
                       "es un solo punto):"),
                ("tex", r"\left(\frac{f}{g}\right)(x)=\frac{x-3}{x^{2}}, \qquad \operatorname{Dom}=\mathbb{R}\setminus\{0\}"),
                ("err", "$(f-g)(x)\\neq(g-f)(x)$: aquí $(g-f)(x)=x^{2}-x+3$. La resta de funciones "
                        "**no** conmuta, igual que la de números."),
                ("md", "**(b)** Ahora los dominios son el punto delicado."),
                ("tex", r"4-x^{2}\ge 0 \iff -2\le x\le 2 \qquad\Longrightarrow\qquad A=[-2,2]"),
                ("tex", r"1+x\ge 0 \iff x\ge -1 \qquad\Longrightarrow\qquad B=[-1,+\infty)"),
                ("tex", r"A\cap B=[-1,2]"),
                ("tex", r"(f+g)(x)=\sqrt{4-x^{2}}+\sqrt{1+x}, \qquad \operatorname{Dom}=[-1,2]"),
                ("tex", r"(f-g)(x)=\sqrt{4-x^{2}}-\sqrt{1+x}, \qquad \operatorname{Dom}=[-1,2]"),
                ("tex", r"(fg)(x)=\sqrt{(4-x^{2})(1+x)}, \qquad \operatorname{Dom}=[-1,2]"),
                ("md", "Cociente: se excluyen los ceros de $g$, o sea $1+x=0$, es decir $x=-1$:"),
                ("tex", r"\left(\frac{f}{g}\right)(x)=\frac{\sqrt{4-x^{2}}}{\sqrt{1+x}}=\sqrt{\frac{4-x^{2}}{1+x}}, \qquad \operatorname{Dom}=(-1,2]"),
                ("err", "**Trampa del inciso (b).** Si se escribe primero "
                        "$\\sqrt{\\dfrac{4-x^{2}}{1+x}}$ y **después** se calcula el dominio pidiendo "
                        "sólo que el radicando sea $\\ge0$, se cuela toda la zona $x<-2$: por ejemplo "
                        "en $x=-3$ el cociente vale $\\tfrac{-5}{-2}=2.5>0$. Pero ahí $f(-3)$ **no "
                        "existe**. El dominio se calcula **antes** de simplificar."),
                ("info", "Regla operativa para el examen: dominio de la combinación = "
                         "(intersección de dominios) $\\setminus$ (ceros del denominador). Nunca al revés."),
            ],
        },
        {
            "t": "Dominio de una combinación",
            "f": "[S] Ejercicios 11, 12, 13 y 14, p. 196",
            "e": [("md", "Hallar el dominio de:\n\n"
                         "(a) $f(x)=\\sqrt{x}+\\sqrt{1-x}$  \n"
                         "(b) $g(x)=\\sqrt{x+1}-\\dfrac{1}{x}$  \n"
                         "(c) $h(x)=(x-3)^{-1/4}$  \n"
                         "(d) $k(x)=\\dfrac{\\sqrt{x+3}}{x-1}$")],
            "s": [
                ("md", "En todos los casos se listan las restricciones y se **intersecan**."),
                ("md", "**(a)** Dos raíces de índice par, dos condiciones:"),
                ("tex", r"x\ge 0 \quad \text{y} \quad 1-x\ge 0 \iff x\le 1"),
                ("tex", r"\operatorname{Dom}(f)=[0,+\infty)\cap(-\infty,1]=[0,1]"),
                ("md", "**(b)** Una raíz y un denominador:"),
                ("tex", r"x+1\ge 0 \iff x\ge -1 \qquad \text{y} \qquad x\neq 0"),
                ("tex", r"\operatorname{Dom}(g)=[-1,0)\cup(0,+\infty)"),
                ("md", "**(c)** El exponente negativo fraccionario esconde **dos** restricciones a la vez:"),
                ("tex", r"(x-3)^{-1/4}=\frac{1}{\sqrt[4]{x-3}}"),
                ("md", "La raíz de índice **par** pide $x-3\\ge0$; estar en el **denominador** pide "
                       "$\\sqrt[4]{x-3}\\neq0$, es decir $x-3\\neq0$. Gana la condición fuerte:"),
                ("tex", r"x-3>0 \iff x>3 \qquad\Longrightarrow\qquad \operatorname{Dom}(h)=(3,+\infty)"),
                ("md", "**(d)** Raíz par arriba, denominador abajo:"),
                ("tex", r"x+3\ge 0 \iff x\ge -3 \qquad \text{y} \qquad x-1\neq 0 \iff x\neq 1"),
                ("tex", r"\operatorname{Dom}(k)=[-3,1)\cup(1,+\infty)"),
                ("warn", "El inciso (c) es el más pedido: un exponente $-1/n$ con $n$ **par** siempre "
                         "produce desigualdad **estricta**."),
            ],
        },
        {
            "t": "Suma gráfica",
            "f": "[S] Ejercicios 15–16, p. 196 · Ejemplo 2, p. 192",
            "e": [("md", "Sean $f(x)=x-2$ y $g(x)=\\sqrt{x}$.\n\n"
                         "(a) Hallar $\\operatorname{Dom}(f+g)$.  \n"
                         "(b) Trazar $f+g$ por **suma gráfica** (sumando ordenadas).  \n"
                         "(c) ¿Dónde corta al eje $x$ la gráfica de $f+g$?")],
            "s": [
                ("md", "**(a)** $\\operatorname{Dom}(f)=\\mathbb{R}$ y "
                       "$\\operatorname{Dom}(g)=[0,+\\infty)$, así que"),
                ("tex", r"\operatorname{Dom}(f+g)=[0,+\infty), \qquad (f+g)(x)=x-2+\sqrt{x}"),
                ("md", "**(b) El método.** Para cada $x$ se toma la altura de $f$ y se le **apila** la "
                       "altura de $g$ (con su signo). Tres anclas hacen el trazo casi solo:"),
                ("md",
                 "| $x$ | $f(x)$ | $g(x)$ | $(f+g)(x)$ | lectura |\n"
                 "|---|---|---|---|---|\n"
                 "| $0$ | $-2$ | $0$ | $-2$ | donde $g=0$, la suma **toca a $f$** |\n"
                 "| $1$ | $-1$ | $1$ | $0$ | las alturas se cancelan: corte con el eje |\n"
                 "| $2$ | $0$ | $\\sqrt2$ | $\\sqrt2$ | donde $f=0$, la suma **toca a $g$** |\n"
                 "| $4$ | $2$ | $2$ | $4$ | ambas positivas: la suma va por arriba |"),
                ("fig", _fig_suma_grafica),
                ("md", "**(c)** Analíticamente, se resuelve $(f+g)(x)=0$. El truco es sustituir "
                       "$u=\\sqrt{x}\\ge0$, con lo que $x=u^{2}$:"),
                ("tex", r"x-2+\sqrt{x}=0 \;\Longrightarrow\; u^{2}+u-2=0 \;\Longrightarrow\; (u+2)(u-1)=0"),
                ("md", "Las raíces son $u=-2$ y $u=1$. La primera se **descarta** porque "
                       "$u=\\sqrt{x}$ no puede ser negativa. Queda:"),
                ("tex", r"\sqrt{x}=1 \;\Longrightarrow\; x=1"),
                ("ok", "La gráfica de $f+g$ corta el eje $x$ en $x=1$, que es justo donde las gráficas "
                       "de $f$ y $g$ están a la misma distancia del eje pero de lados opuestos "
                       "($f(1)=-1$, $g(1)=1$)."),
                ("info", "Las tres lecturas de la tabla son generales y valen para cualquier par de "
                         "funciones: donde una se anula, la suma coincide con la otra; donde son "
                         "opuestas, la suma cruza el eje."),
            ],
        },
        {
            "t": "Sumas y productos de funciones pares e impares",
            "f": "[S] Ejercicios 91 y 92, p. 190",
            "e": [("md", "Usando la definición $(f+g)(x)=f(x)+g(x)$ y $(fg)(x)=f(x)g(x)$, demostrar "
                         "o refutar:\n\n"
                         "(a) si $f$ y $g$ son pares, $f+g$ es par  \n"
                         "(b) si $f$ y $g$ son impares, $f+g$ es impar  \n"
                         "(c) si una es par y la otra impar, ¿qué se puede decir de $f+g$?  \n"
                         "(d) ¿qué pasa con el **producto** en los tres casos?")],
            "s": [
                ("md", "Recordatorio: $f$ es **par** si $f(-x)=f(x)$; es **impar** si $f(-x)=-f(x)$ "
                       "([S] p. 186). Todas las demostraciones son evaluar la combinación en $-x$."),
                ("md", "**(a)** Sea $h=f+g$ con $f,g$ pares:"),
                ("tex", r"h(-x)=f(-x)+g(-x)=f(x)+g(x)=h(x)"),
                ("ok", "**Sí**, la suma de pares es par."),
                ("md", "**(b)** Con $f,g$ impares:"),
                ("tex", r"h(-x)=f(-x)+g(-x)=-f(x)-g(x)=-\bigl(f(x)+g(x)\bigr)=-h(x)"),
                ("ok", "**Sí**, la suma de impares es impar."),
                ("md", "**(c)** En general **ninguna de las dos**. Contraejemplo mínimo: $f(x)=x^{2}$ "
                       "(par) y $g(x)=x$ (impar) dan $h(x)=x^{2}+x$, que no es par ni impar "
                       "(ya se vio: $h(1)=2$, $h(-1)=0$)."),
                ("warn", "Hay una excepción: si una de las dos es la **función cero** (que es par e "
                         "impar a la vez), la suma hereda el carácter de la otra."),
                ("md", "**(d) Producto.** Con $P=fg$:"),
                ("tex", r"\text{par}\cdot\text{par}: \quad P(-x)=f(x)g(x)=P(x) \quad \Rightarrow\ \textbf{par}"),
                ("tex", r"\text{impar}\cdot\text{impar}: \quad P(-x)=(-f(x))(-g(x))=f(x)g(x)=P(x) \quad \Rightarrow\ \textbf{par}"),
                ("tex", r"\text{par}\cdot\text{impar}: \quad P(-x)=f(x)\,(-g(x))=-P(x) \quad \Rightarrow\ \textbf{impar}"),
                ("ok", "**Los signos se comportan como suma de exponentes**, tal como pasa con "
                       "$x^{m}x^{n}=x^{m+n}$: par+par = par, impar+impar = par, par+impar = impar. "
                       "Esa analogía es también la respuesta al Ejercicio 93 (p. 190): $x^{n}$ es par "
                       "si $n$ es par e impar si $n$ es impar, y de ahí vienen los nombres."),
                ("info", "**Diferencia importante:** el producto se lleva bien con la paridad, la "
                         "suma sólo cuando los dos sumandos son del mismo tipo. La clasificación "
                         "algebraica de la paridad se trabaja en la pestaña 5."),
            ],
        },
        {
            "t": "Cadena de transformaciones",
            "f": "[D] diapositivas 39, 41–42 · [S] Ejemplo 6, p. 184",
            "e": [("md", "Con $f(x)=x^{2}$, describir paso a paso la gráfica de "
                         "$g(x)=-2f(x-1)+3$ y hallar su vértice, rango y ejes de simetría.")],
            "s": [
                ("md", "Primero, la fórmula explícita:"),
                ("tex", r"g(x)=-2(x-1)^{2}+3"),
                ("md", "**El orden importa.** Se aplica de adentro hacia afuera, igual que al evaluar:"),
                ("md",
                 "1. $f(x-1)=(x-1)^2$ → traslación **horizontal 1 a la derecha**. Vértice pasa de "
                 "$(0,0)$ a $(1,0)$.\n"
                 "2. $2f(x-1)$ → **alargamiento vertical** factor 2. La parábola se hace más angosta.\n"
                 "3. $-2f(x-1)$ → **reflexión respecto al eje $x$**. Ahora abre hacia abajo.\n"
                 "4. $-2f(x-1)+3$ → traslación **vertical 3 hacia arriba**. Vértice final $(1,3)$."),
                ("fig", _fig_transformacion),
                ("md", "**Lecturas de la gráfica final:**"),
                ("md", "- Vértice: $(1,3)$, que es un **máximo** (abre hacia abajo).\n"
                       "- $\\operatorname{Dom}(g)=\\mathbb{R}$.\n"
                       "- $\\operatorname{Ran}(g)=(-\\infty,3]$.\n"
                       "- Eje de simetría: la recta vertical $x=1$."),
                ("warn", "**Trampa clásica:** $f(x-1)$ mueve a la **derecha**, no a la izquierda. "
                         "Razón: para que el argumento valga $0$ (donde estaba el vértice) hace falta "
                         "$x=1$, no $x=-1$. Es decir, se necesita una $x$ mayor."),
                ("err", "Las traslaciones verticales y las reflexiones **no conmutan**: "
                        "$-2f(x)+3$ es distinto de $-2\\bigl(f(x)+3\\bigr)=-2f(x)-6$."),
            ],
        },
        {
            "t": "Escribir la ecuación de la gráfica transformada",
            "f": "[S] Ejercicios 47, 49, 51 y 53, p. 188 · Ejercicio 85, p. 189",
            "e": [("md", "Aplicar a $f$ las transformaciones indicadas **en el orden dado** y escribir "
                         "la ecuación final:\n\n"
                         "(a) $f(x)=\\sqrt{x}$; desplazar 2 unidades a la izquierda  \n"
                         "(b) $f(x)=|x|$; desplazar 3 a la derecha y 1 hacia arriba  \n"
                         "(c) $f(x)=\\sqrt[4]{x}$; reflejar en el eje $y$ y desplazar 1 hacia arriba  \n"
                         "(d) $f(x)=x^{2}$; alargar verticalmente factor 2, desplazar 2 hacia abajo, "
                         "desplazar 3 a la derecha  \n"
                         "(e) A partir de $f(x)=x^{2}-4$, obtener la gráfica de $g(x)=|x^{2}-4|$")],
            "s": [
                ("md", "**(a)** «A la izquierda $c$» es $f(x+c)$:"),
                ("tex", r"y=\sqrt{x+2}, \qquad \operatorname{Dom}=[-2,+\infty)"),
                ("md", "**(b)** Derecha 3 → $f(x-3)$; arriba 1 → $+1$:"),
                ("tex", r"y=|x-3|+1"),
                ("md", "**(c)** Reflexión en el eje $y$ es $f(-x)$; luego se suma 1:"),
                ("tex", r"y=\sqrt[4]{-x}+1, \qquad \operatorname{Dom}=(-\infty,0]"),
                ("warn", "En (c) el dominio se voltea junto con la gráfica: sólo sobreviven los "
                         "$x\\le0$. Reflejar en el eje $y$ **sí** cambia el dominio; reflejar en el "
                         "eje $x$ cambia el rango."),
                ("md", "**(d)** Paso a paso, respetando el orden del enunciado:"),
                ("tex", r"x^{2} \ \xrightarrow{\ \times 2\ }\ 2x^{2} \ \xrightarrow{\ -2\ }\ 2x^{2}-2 \ \xrightarrow{\ x\to x-3\ }\ 2(x-3)^{2}-2"),
                ("err", "**El orden no es decorativo.** Si se hubiera bajado 2 *antes* de alargar, el "
                        "resultado sería $2(x^{2}-2)=2x^{2}-4$, con vértice en $-4$ y no en $-2$. "
                        "Alargamiento vertical y traslación vertical **no conmutan**."),
                ("info", "En cambio, una traslación **horizontal** sí conmuta con cualquier operación "
                         "vertical: por eso en (d) daba igual desplazar 3 a la derecha al principio "
                         "o al final."),
                ("md", "**(e)** El valor absoluto deja intacto lo que está **sobre** el eje $x$ y "
                       "**refleja hacia arriba** lo que está debajo. Como"),
                ("tex", r"x^{2}-4<0 \iff -2<x<2"),
                ("md", "la gráfica de $g$ coincide con la de $f$ fuera de $(-2,2)$ y es su reflejo "
                       "dentro. El vértice $(0,-4)$ se convierte en $(0,4)$, y los ceros $x=\\pm2$ se "
                       "vuelven picos."),
                ("fig", _fig_valor_absoluto),
                ("ok", "Consecuencia inmediata: $\\operatorname{Ran}(f)=[-4,+\\infty)$ pero "
                       "$\\operatorname{Ran}(g)=[0,+\\infty)$. Y $g$ ya no es derivable en "
                       "$x=\\pm2$ (los picos), detalle que reaparece en la Unidad 3."),
            ],
        },
        {
            "t": "Alargamiento y contracción horizontales",
            "f": "[S] Ejercicios 65–66, p. 189 · Ejercicio 73, p. 189",
            "e": [("md", "Sea $f(x)=\\sqrt{2x-x^{2}}$, cuyo dominio es $[0,2]$ y cuyo rango es $[0,1]$.\n\n"
                         "(a) Identificar la curva.  \n"
                         "(b) Describir y trazar $y=f(2x)$ y $y=f\\!\\left(\\tfrac12 x\\right)$, con sus "
                         "dominios.  \n"
                         "(c) ¿Cambia el rango?  \n"
                         "(d) ¿Qué sería $y=f(-x)$?")],
            "s": [
                ("md", "**(a)** Se eleva al cuadrado para reconocerla:"),
                ("tex", r"y=\sqrt{2x-x^{2}} \;\Longrightarrow\; y^{2}=2x-x^{2} \;\Longrightarrow\; x^{2}-2x+y^{2}=0"),
                ("tex", r"(x-1)^{2}+y^{2}=1, \qquad y\ge 0"),
                ("ok", "Es el **semicírculo superior** de centro $(1,0)$ y radio 1. Por eso el dominio "
                       "es $[0,2]$ y el rango $[0,1]$."),
                ("md", "**(b) $y=f(2x)$.** El dominio se obtiene pidiendo que el **argumento** caiga "
                       "en el dominio original:"),
                ("tex", r"0\le 2x\le 2 \iff 0\le x\le 1 \qquad\Longrightarrow\qquad \operatorname{Dom}=[0,1]"),
                ("md", "El intervalo se redujo a la mitad: es una **contracción horizontal de factor "
                       "$\\tfrac12$**. Explícitamente:"),
                ("tex", r"f(2x)=\sqrt{4x-4x^{2}}=2\sqrt{x-x^{2}}"),
                ("md", "**$y=f\\!\\left(\\tfrac12x\\right)$.** Mismo razonamiento:"),
                ("tex", r"0\le \tfrac{1}{2}x\le 2 \iff 0\le x\le 4 \qquad\Longrightarrow\qquad \operatorname{Dom}=[0,4]"),
                ("md", "El intervalo se duplicó: **alargamiento horizontal de factor 2**."),
                ("fig", _fig_horizontales),
                ("warn", "**Lo contraintuitivo:** $f(cx)$ con $c>1$ **contrae** (no alarga), y con "
                         "$0<c<1$ **alarga**. La razón operativa está a la vista en el despeje: para "
                         "que $2x$ recorra todo $[0,2]$, a $x$ le basta recorrer $[0,1]$."),
                ("md", "**(c)** **No.** Las transformaciones horizontales sólo tocan la variable de "
                       "entrada; las alturas son las mismas. En los tres casos "
                       "$\\operatorname{Ran}=[0,1]$."),
                ("md", "**(d)** $y=f(-x)$ es la reflexión en el eje $y$: el semicírculo pasa a tener "
                       "centro $(-1,0)$ y dominio"),
                ("tex", r"0\le -x\le 2 \iff -2\le x\le 0 \qquad\Longrightarrow\qquad \operatorname{Dom}=[-2,0]"),
                ("info", "Regla mnemotécnica: **lo que está pegado a la $x$ actúa horizontalmente y "
                         "al revés de lo que parece; lo que está fuera actúa verticalmente y tal como "
                         "parece.**"),
            ],
        },
        {
            "t": "Del enunciado a la clasificación (caso aplicado)",
            "f": "estilo [S] §2.7",
            "e": [("md", "Una empresa asigna a cada empleado un número de nómina. Sea $N$ la función "
                         "«empleado $\\mapsto$ número de nómina», del conjunto de empleados al conjunto "
                         "de números asignados.\n\n"
                         "(a) ¿Debe ser inyectiva? (b) ¿Debe ser suprayectiva? (c) ¿Qué significaría "
                         "que fuera biyectiva? (d) ¿Es función la regla «empleado $\\mapsto$ número "
                         "telefónico»?")],
            "s": [
                ("md", "**(a)** Sí, y es un requisito **de diseño**: si dos empleados compartieran "
                       "número, el número no identificaría a nadie. Inyectividad = «el código "
                       "identifica unívocamente»."),
                ("md", "**(b)** Depende del codominio declarado. Si el codominio es «los números "
                       "efectivamente asignados», es suprayectiva por construcción. Si el codominio "
                       "fuera «todos los enteros de 1 a 99999», no lo sería: sobrarían números sin "
                       "dueño."),
                ("md", "**(c)** Biyectiva significaría correspondencia perfecta: cada empleado con un "
                       "número y cada número con un empleado. Eso es lo que permite **invertir**: dado "
                       "un número, recuperar al empleado."),
                ("md", "**(d)** **No es función** si algún empleado tiene varios teléfonos: una entrada "
                       "produciría varias salidas. Tampoco lo es si alguno no tiene teléfono: esa "
                       "entrada no tendría salida."),
                ("info", "Este ejercicio es útil al inicio de la sesión: conecta las tres propiedades "
                         "con su significado operativo antes de entrar al álgebra."),
            ],
        },
    ]
    mostrar_ejercicios(ejercicios_u3, abrir_todo)

# ==================================================================================
# TAB 4 — COMPOSICIÓN E INVERSA
# ==================================================================================
with TABS[4]:
    st.header("4 · Composición e inversa")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Composición")
        st.latex(r"(f\circ g)(x)=f\bigl(g(x)\bigr)")
        st.markdown("Se aplica **primero $g$** (la de adentro) y **luego $f$**.")
        st.latex(r"\operatorname{Dom}(f\circ g)=\bigl\{x\in\operatorname{Dom}(g) : g(x)\in\operatorname{Dom}(f)\bigr\}")
        st.error("En general $f\\circ g \\neq g\\circ f$: la composición **no es conmutativa**.")
        st.warning(
            "$\\operatorname{Dom}(f\\circ g)$ puede ser **estrictamente menor** que "
            "$\\operatorname{Dom}(g)$: se descartan los $x$ cuya imagen $g(x)$ cae fuera del "
            "dominio de $f$. Calcular el dominio **antes** de simplificar la fórmula."
        )
    with c2:
        st.markdown("#### Inversa")
        st.markdown("Si $f\\colon A\\to B$ es **biyectiva**, existe una única $f^{-1}\\colon B\\to A$ con")
        st.latex(r"f^{-1}(y)=x \iff f(x)=y")
        st.latex(r"(f^{-1}\circ f)(x)=x \ \ \forall x\in A, \qquad (f\circ f^{-1})(y)=y \ \ \forall y\in B")
        st.markdown(
            """
| | Dominio | Rango |
|---|---|---|
| $f$ | $A$ | $B$ |
| $f^{-1}$ | $B$ | $A$ |

**Dominio y rango se intercambian.** La gráfica de $f^{-1}$ es la reflexión de la de $f$
respecto de la recta $y=x$.
"""
        )
        st.error("$f^{-1}(x)\\neq\\dfrac{1}{f(x)}$. El $-1$ es notación de inversa, no exponente.")

    st.markdown("#### Método para hallar la inversa")
    st.markdown(
        "1. Escribir $y=f(x)$.  \n"
        "2. **Verificar que $f$ sea inyectiva** (si no, restringir el dominio primero).  \n"
        "3. Despejar $x$ en términos de $y$.  \n"
        "4. Intercambiar nombres: $f^{-1}(x)=\\dots$  \n"
        "5. **Verificar** con $f(f^{-1}(x))=x$, y declarar el dominio de $f^{-1}$ (= rango de $f$)."
    )

    st.markdown("---")
    st.subheader("Ejemplos resueltos")

    def _fig_reflexion():
        fig, ax = nueva_fig(figsize=(4.6, 4.4))
        x = np.linspace(-1.5, 3.2, 300)
        ax.plot(x, 2 * x + 1, color=AZUL, lw=2, label=r"$f(x)=2x+1$")
        ax.plot(x, (x - 1) / 2, color=OCRE, lw=2, label=r"$f^{-1}(x)=\frac{x-1}{2}$")
        ax.plot(x, x, color=VERDE, lw=1.2, ls="--", label=r"$y=x$")
        ax.plot([2], [5], "o", color=AZUL, ms=7)
        ax.plot([5], [2], "o", color=OCRE, ms=7)
        ax.annotate("(2,5)", (2, 5), textcoords="offset points", xytext=(6, 4), fontsize=8)
        ax.annotate("(5,2)", (5, 2), textcoords="offset points", xytext=(6, -12), fontsize=8)
        ax.set_xlim(-2, 6.5)
        ax.set_ylim(-2, 6.5)
        ax.set_aspect("equal")
        ax.legend(fontsize=8, loc="upper left")
        fig.tight_layout()
        return fig

    ejemplos_u4 = [
        {
            "t": "Composición en los dos órdenes",
            "f": "[D] diapositiva 46",
            "c": [
                ("md", "Sean $f(x)=x^{2}+1$ y $g(x)=2x-3$. Calcular $f\\circ g$ y $g\\circ f$."),
                ("md", "**$f\\circ g$:** primero $g$, luego $f$. Se sustituye $g(x)$ donde $f$ pide $x$:"),
                ("tex", r"(f\circ g)(x)=f(g(x))=f(2x-3)=(2x-3)^{2}+1"),
                ("tex", r"=4x^{2}-12x+9+1=4x^{2}-12x+10"),
                ("md", "**$g\\circ f$:** ahora al revés."),
                ("tex", r"(g\circ f)(x)=g(f(x))=g(x^{2}+1)=2(x^{2}+1)-3=2x^{2}-1"),
                ("md", "**Verificación numérica en $x=2$** (siempre conviene, detecta errores de signo):"),
                ("md", "- $f\\circ g$: $g(2)=1$, luego $f(1)=1^2+1=2$. Con la fórmula: "
                       "$4(4)-24+10=2$ ✓\n"
                       "- $g\\circ f$: $f(2)=5$, luego $g(5)=7$. Con la fórmula: $2(4)-1=7$ ✓"),
                ("err", "$4x^{2}-12x+10\\neq2x^{2}-1$: la composición **no** es conmutativa. "
                        "Además ambos dominios son $\\mathbb{R}$ aquí, pero eso es coincidencia."),
            ],
        },
        {
            "t": "Composición donde el dominio se encoge",
            "f": "[D] diapositiva 47",
            "c": [
                ("md", "Sean $f(x)=\\sqrt{x+1}$ y $g(x)=x^{2}-4$. Hallar ambas composiciones **con sus "
                       "dominios**."),
                ("md", "**$f\\circ g$:**"),
                ("tex", r"(f\circ g)(x)=f(x^{2}-4)=\sqrt{(x^{2}-4)+1}=\sqrt{x^{2}-3}"),
                ("md", "Dominio: se necesita $x^{2}-3\\ge0$, es decir $|x|\\ge\\sqrt3$:"),
                ("tex", r"\operatorname{Dom}(f\circ g)=\left(-\infty,-\sqrt{3}\,\right]\cup\left[\sqrt{3},+\infty\right)"),
                ("md", "**$g\\circ f$:**"),
                ("tex", r"(g\circ f)(x)=g\!\left(\sqrt{x+1}\right)=\left(\sqrt{x+1}\right)^{2}-4=x+1-4=x-3"),
                ("warn", "**Aquí está la trampa del tema.** La fórmula simplificada $x-3$ parece tener "
                         "dominio $\\mathbb{R}$, pero para poder calcular $f(x)$ **primero** hacía falta "
                         "$x+1\\ge0$. La restricción sobrevive a la simplificación:"),
                ("tex", r"\operatorname{Dom}(g\circ f)=[-1,+\infty), \quad \textbf{no } \mathbb{R}"),
                ("ok", "$f\\circ g\\neq g\\circ f$, y difieren **tanto en la regla como en el dominio**."),
                ("info", "Método seguro: calcular el dominio con la **definición** "
                         "($x\\in\\operatorname{Dom}(g)$ y $g(x)\\in\\operatorname{Dom}(f)$) **antes** "
                         "de simplificar la expresión."),
            ],
        },
        {
            "t": "Inversa e interpretación geométrica",
            "f": "[D] diapositivas 57 y 59",
            "c": [
                ("md", "Hallar la inversa de $f(x)=2x+1$ y verificarla."),
                ("md", "**Paso 1.** $y=2x+1$.  **Paso 2.** Es lineal con pendiente $\\neq0$: biyectiva."),
                ("md", "**Paso 3.** Despejar $x$:"),
                ("tex", r"y-1=2x \;\Longrightarrow\; x=\frac{y-1}{2}"),
                ("md", "**Paso 4.** Renombrar:"),
                ("tex", r"f^{-1}(x)=\frac{x-1}{2}"),
                ("md", "**Paso 5. Verificación en ambos sentidos** (esto es obligatorio):"),
                ("tex", r"f\bigl(f^{-1}(x)\bigr)=2\cdot\frac{x-1}{2}+1=(x-1)+1=x\ \checkmark"),
                ("tex", r"f^{-1}\bigl(f(x)\bigr)=\frac{(2x+1)-1}{2}=\frac{2x}{2}=x\ \checkmark"),
                ("fig", _fig_reflexion),
                ("md", "**Por qué la reflexión en $y=x$:** si $(a,b)$ está en la gráfica de $f$, "
                       "entonces $f(a)=b$, luego $f^{-1}(b)=a$, o sea $(b,a)$ está en la gráfica de "
                       "$f^{-1}$. Y reflejar $(a,b)$ en $y=x$ produce exactamente $(b,a)$."),
                ("info", "En la figura: $(2,5)$ está en $f$ y $(5,2)$ en $f^{-1}$."),
            ],
        },
    ]
    mostrar_ejemplos(ejemplos_u4)

    st.markdown("---")
    st.subheader("Ejercicios")

    def _fig_inv_cuadratica():
        fig, ax = nueva_fig(figsize=(4.6, 4.4))
        x = np.linspace(2, 4, 200)
        xi = np.linspace(1, 5, 300)
        ax.plot(x, (x - 2) ** 2 + 1, color=AZUL, lw=2, label=r"$f(x)=(x-2)^2+1,\ x\geq 2$")
        ax.plot(xi, 2 + np.sqrt(xi - 1), color=OCRE, lw=2, label=r"$f^{-1}(x)=2+\sqrt{x-1}$")
        ax.plot(np.linspace(0, 5.5, 10), np.linspace(0, 5.5, 10), color=VERDE, ls="--", lw=1.1)
        ax.set_xlim(0, 5.5)
        ax.set_ylim(0, 5.5)
        ax.set_aspect("equal")
        ax.legend(fontsize=7.5, loc="lower right")
        fig.tight_layout()
        return fig

    def _fig_area_tiempo():
        fig, ax = nueva_fig(xlabel="t (s)", ylabel=r"A (cm$^2$)")
        t = np.linspace(0, 5, 300)
        ax.plot(t, np.pi * (2 * t + 1) ** 2, color=AZUL, lw=2)
        ax.axhline(100 * np.pi, color=VERDE, ls="--")
        ax.plot([4.5], [100 * np.pi], "o", color=VERDE, ms=8)
        ax.annotate(r"$t=4.5$ s", (4.5, 100 * np.pi), textcoords="offset points",
                    xytext=(-52, 12), color=VERDE)
        ax.set_title(r"$(A\circ r)(t)=\pi(2t+1)^2$", fontsize=10)
        fig.tight_layout()
        return fig

    ejercicios_u4 = [
        {
            "t": "Composición evaluada y autocomposición",
            "f": "[D] diapositiva 52",
            "e": [("md", "Sean $f(x)=x^{2}-x$ y $g(x)=x+2$. Calcular $(f\\circ g)(3)$, "
                         "$(g\\circ f)(3)$ y $(f\\circ f)(x)$.")],
            "s": [
                ("md", "**$(f\\circ g)(3)$** — de adentro hacia afuera, no hace falta la fórmula general:"),
                ("tex", r"g(3)=3+2=5 \qquad\Longrightarrow\qquad (f\circ g)(3)=f(5)=5^{2}-5=20"),
                ("md", "**$(g\\circ f)(3)$** — orden invertido:"),
                ("tex", r"f(3)=3^{2}-3=6 \qquad\Longrightarrow\qquad (g\circ f)(3)=g(6)=6+2=8"),
                ("err", "$(f\\circ g)(3)=20 \\neq 8=(g\\circ f)(3)$: confirmación numérica de que la "
                        "composición no conmuta."),
                ("md", "**$(f\\circ f)(x)$** — se compone $f$ consigo misma; el bloque que entra es "
                       "$x^{2}-x$:"),
                ("tex", r"(f\circ f)(x)=f(x^{2}-x)=(x^{2}-x)^{2}-(x^{2}-x)"),
                ("md", "Se expande el cuadrado:"),
                ("tex", r"(x^{2}-x)^{2}=x^{4}-2x^{3}+x^{2}"),
                ("tex", r"(f\circ f)(x)=x^{4}-2x^{3}+x^{2}-x^{2}+x=x^{4}-2x^{3}+x"),
                ("md", "Dominio: $\\mathbb{R}$ (polinomios en todas las etapas)."),
                ("info", "Comprobación rápida: $(f\\circ f)(2)=16-16+2=2$. Directo: $f(2)=2$, "
                         "$f(2)=2$ ✓ (el $2$ resulta ser punto fijo de $f$)."),
            ],
        },
        # ==================================================================================
# INSERCIÓN EN LA PESTAÑA 4 (Composición e inversa)
#
# Pegar este diccionario dentro de la lista `ejercicios_u4`, JUSTO ANTES del
# ejercicio titulado "Inversa de una función racional (y una afirmación que hay
# que revisar)".  Así el alumno ve primero el método limpio del libro y después
# se enfrenta a la afirmación falsa de la diapositiva 60(b).
# ==================================================================================

        {
            "t": "Inversa de una función racional (método del libro)",
            "f": "[S] Ejemplo 8, p. 203",
            "e": [("md", "Encontrar la inversa de $f(x)=\\dfrac{2x+3}{x-1}$, declarar dominios y "
                         "rangos, y verificar el resultado.")],
            "s": [
                ("md", "**Paso 0. ¿Es inyectiva?** Antes de despejar hay que saber que la inversa "
                       "existe. Supóngase $f(x_1)=f(x_2)$ con $x_1,x_2\\neq1$:"),
                ("tex", r"\frac{2x_{1}+3}{x_{1}-1}=\frac{2x_{2}+3}{x_{2}-1}"),
                ("md", "Multiplicación cruzada (los denominadores no son cero) y expansión:"),
                ("tex", r"(2x_{1}+3)(x_{2}-1)=(2x_{2}+3)(x_{1}-1)"),
                ("tex", r"2x_{1}x_{2}-2x_{1}+3x_{2}-3=2x_{1}x_{2}-2x_{2}+3x_{1}-3"),
                ("md", "Se cancelan $2x_1x_2$ y $-3$ en ambos lados:"),
                ("tex", r"-2x_{1}+3x_{2}=-2x_{2}+3x_{1} \;\Longrightarrow\; 5x_{2}=5x_{1} \;\Longrightarrow\; x_{1}=x_{2}\ \checkmark"),
                ("md", "**Paso 1. Escribir $y=f(x)$ y despejar $x$.** Éste es el método de la "
                       "p. 202 del libro, y el paso clave es **agrupar los términos con $x$** para "
                       "poder factorizarla."),
                ("tex", r"y=\frac{2x+3}{x-1}"),
                ("tex", r"y(x-1)=2x+3 \qquad (\text{multiplicar por } x-1)"),
                ("tex", r"yx-y=2x+3 \qquad (\text{desarrollar})"),
                ("tex", r"yx-2x=y+3 \qquad (\text{términos con } x \text{ a la izquierda})"),
                ("tex", r"x(y-2)=y+3 \qquad (\text{factorizar } x)"),
                ("tex", r"x=\frac{y+3}{y-2} \qquad (\text{dividir entre } y-2)"),
                ("md", "**Paso 2. Intercambiar los nombres de las variables:**"),
                ("tex", r"f^{-1}(x)=\frac{x+3}{x-2}"),
                ("md", "**Paso 3. Dominios y rangos** (se intercambian). El $1$ sale del dominio de "
                       "$f$ por el denominador; el $2$ sale del rango porque es la **asíntota "
                       "horizontal** (cociente de coeficientes principales, $2/1$):"),
                ("tex", r"\operatorname{Dom}(f)=\mathbb{R}\setminus\{1\}, \qquad \operatorname{Ran}(f)=\mathbb{R}\setminus\{2\}"),
                ("tex", r"\operatorname{Dom}(f^{-1})=\mathbb{R}\setminus\{2\}, \qquad \operatorname{Ran}(f^{-1})=\mathbb{R}\setminus\{1\}"),
                ("md", "**Paso 4. Verificación** con la Propiedad de la Función Inversa "
                       "($f(f^{-1}(x))=x$). Conviene trabajar numerador y denominador por separado, "
                       "poniendo todo sobre el común denominador $x-2$:"),
                ("tex", r"\text{num: } 2\cdot\frac{x+3}{x-2}+3=\frac{2(x+3)+3(x-2)}{x-2}=\frac{2x+6+3x-6}{x-2}=\frac{5x}{x-2}"),
                ("tex", r"\text{den: } \frac{x+3}{x-2}-1=\frac{(x+3)-(x-2)}{x-2}=\frac{5}{x-2}"),
                ("tex", r"f\bigl(f^{-1}(x)\bigr)=\frac{5x/(x-2)}{5/(x-2)}=\frac{5x}{5}=x\ \checkmark"),
                ("md", "**Comprobación numérica rápida:** $f(3)=\\dfrac{9}{2}$, y "
                       "$f^{-1}\\!\\left(\\tfrac92\\right)=\\dfrac{\\tfrac92+3}{\\tfrac92-2}="
                       "\\dfrac{15/2}{5/2}=3$ ✓"),
                ("warn", "**$f$ tampoco es su propia inversa**, aunque $f^{-1}$ tenga la misma forma "
                         "$\\dfrac{ax+b}{cx+d}$. Con la misma técnica:"),
                ("tex", r"f\bigl(f(x)\bigr)=\frac{2\cdot\frac{2x+3}{x-1}+3}{\frac{2x+3}{x-1}-1}=\frac{\frac{2(2x+3)+3(x-1)}{x-1}}{\frac{(2x+3)-(x-1)}{x-1}}=\frac{7x+3}{x+4}\ \neq\ x"),
                ("info", "Compárese con el ejercicio siguiente, $\\dfrac{2x+1}{x-3}$: mismo método, "
                         "misma familia (**homografías**), y la misma conclusión sobre la afirmación "
                         "«es su propia inversa». Un caso en que sí ocurre es "
                         "$q(x)=\\sqrt{9-x^{2}}$ con $0\\le x\\le3$ (pestaña 3, ejercicio 7)."),
            ],
        },  
        {
            "t": "Composición con dominios distintos",
            "f": "[D] diapositivas 50–51",
            "e": [("md", "Sean $f(x)=\\dfrac{1}{x+1}$ y $g(x)=\\sqrt{x}$. Hallar $(f\\circ g)(x)$ y "
                         "$(g\\circ f)(x)$ con sus dominios.")],
            "s": [
                ("md", "**$f\\circ g$:**"),
                ("tex", r"(f\circ g)(x)=f\!\left(\sqrt{x}\right)=\frac{1}{\sqrt{x}+1}"),
                ("md", "Dominio, con la definición:"),
                ("md", "1. $x\\in\\operatorname{Dom}(g)$: hace falta $x\\ge0$.\n"
                       "2. $g(x)\\in\\operatorname{Dom}(f)$: hace falta $\\sqrt x\\neq-1$, que se "
                       "cumple **automáticamente** porque $\\sqrt x\\ge0$."),
                ("tex", r"\operatorname{Dom}(f\circ g)=[0,+\infty)"),
                ("md", "**$g\\circ f$:**"),
                ("tex", r"(g\circ f)(x)=g\!\left(\frac{1}{x+1}\right)=\sqrt{\frac{1}{x+1}}"),
                ("md", "Dominio:"),
                ("md", "1. $x\\in\\operatorname{Dom}(f)$: $x\\neq-1$.\n"
                       "2. $f(x)\\in\\operatorname{Dom}(g)$: hace falta $\\dfrac{1}{x+1}\\ge0$. Como el "
                       "numerador es $1>0$, esto obliga a $x+1>0$ (no puede ser $=0$)."),
                ("tex", r"x+1>0 \iff x>-1 \qquad\Longrightarrow\qquad \operatorname{Dom}(g\circ f)=(-1,+\infty)"),
                ("ok", "Las fórmulas son distintas y los dominios también: "
                       "$[0,\\infty)$ contra $(-1,\\infty)$."),
                ("warn", "Un fraccionario $\\dfrac{1}{x+1}$ **nunca** vale 0, así que la desigualdad "
                         "$\\ge0$ se vuelve $>0$ de forma efectiva. Ese detalle decide si el extremo "
                         "entra o no."),
            ],
        },
        {
            "t": "Descomposición: escribir $h$ como composición",
            "f": "[D] diapositivas 48–49 y 53",
            "e": [("md", "Expresar cada función como composición de funciones más simples:\n\n"
                         "(a) $h(x)=\\cos^{2}(3x+1)$  (b) $h(x)=\\sqrt{\\operatorname{sen}(x^{2})}$  "
                         "(c) $h(x)=(2x+5)^{10}$  (d) $h(x)=\\dfrac{1}{(x-1)^{3}}$")],
            "s": [
                ("md", "**Estrategia:** identificar las capas leyendo **de adentro hacia afuera**, tal "
                       "como se evaluaría con calculadora."),
                ("md", "**(a)** Al evaluar $\\cos^{2}(3x+1)$ en $x=1$ se haría: $3(1)+1=4$; luego "
                       "$\\cos 4$; luego elevar al cuadrado. Esas son las tres capas:"),
                ("tex", r"k(x)=3x+1, \qquad g(u)=\cos u, \qquad f(v)=v^{2}"),
                ("tex", r"(f\circ g\circ k)(x)=f\bigl(g(3x+1)\bigr)=f\bigl(\cos(3x+1)\bigr)=\cos^{2}(3x+1)\ \checkmark"),
                ("md", "**(b)** Mismo esquema:"),
                ("tex", r"k(x)=x^{2}, \qquad g(u)=\operatorname{sen} u, \qquad f(v)=\sqrt{v}"),
                ("warn", "Aquí el dominio **no** es $\\mathbb{R}$: hace falta $\\operatorname{sen}(x^2)\\ge0$, "
                         "lo que da una unión infinita de intervalos."),
                ("md", "**(c)** Dos capas:"),
                ("tex", r"g(x)=2x+5, \qquad f(u)=u^{10} \qquad\Longrightarrow\qquad f(g(x))=(2x+5)^{10}\ \checkmark"),
                ("md", "**(d)** Dos capas:"),
                ("tex", r"g(x)=x-1, \qquad f(u)=\frac{1}{u^{3}} \qquad\Longrightarrow\qquad f(g(x))=\frac{1}{(x-1)^{3}}\ \checkmark"),
                ("info", "**La descomposición no es única.** En (c) también sirve $g(x)=(2x+5)^{2}$ con "
                         "$f(u)=u^{5}$. Se busca la más simple y útil."),
                ("ok", "**Por qué importa:** la Regla de la Cadena deriva $h$ usando las derivadas de "
                       "cada capa: $h'(x)=f'(g(k))\\cdot g'(k)\\cdot k'(x)$. Identificar bien las capas "
                       "es el primer paso, y el que más errores causa en Unidad 3."),
            ],
        },
        {
            "t": "Inversa de una función racional (y una afirmación que hay que revisar)",
            "f": "[D] diapositiva 60(b)",
            "e": [("md", "Sea $f(x)=\\dfrac{2x+1}{x-3}$.\n\n"
                         "(a) Hallar $f^{-1}$ y su dominio.  \n"
                         "(b) La diapositiva afirma que «esta función es su propia inversa». "
                         "Verificar si es cierto.")],
            "s": [
                ("md", "**(a)** Se escribe $y=\\dfrac{2x+1}{x-3}$ y se despeja $x$."),
                ("tex", r"y(x-3)=2x+1"),
                ("tex", r"yx-3y=2x+1"),
                ("md", "Se agrupan los términos con $x$ de un lado:"),
                ("tex", r"yx-2x=1+3y \;\Longrightarrow\; x(y-2)=3y+1"),
                ("tex", r"x=\frac{3y+1}{y-2} \qquad\Longrightarrow\qquad f^{-1}(x)=\frac{3x+1}{x-2}"),
                ("md", "**Dominios y rangos** (se intercambian):"),
                ("tex", r"\operatorname{Dom}(f)=\mathbb{R}\setminus\{3\}, \quad \operatorname{Ran}(f)=\mathbb{R}\setminus\{2\}"),
                ("tex", r"\operatorname{Dom}(f^{-1})=\mathbb{R}\setminus\{2\}, \quad \operatorname{Ran}(f^{-1})=\mathbb{R}\setminus\{3\}"),
                ("md", "**Verificación:**"),
                ("tex", r"f\bigl(f^{-1}(x)\bigr)=\frac{2\cdot\frac{3x+1}{x-2}+1}{\frac{3x+1}{x-2}-3}=\frac{\frac{6x+2+x-2}{x-2}}{\frac{3x+1-3x+6}{x-2}}=\frac{7x}{7}=x\ \checkmark"),
                ("md", "**(b)** «Ser su propia inversa» (ser una **involución**) significaría "
                       "$f\\circ f=\\mathrm{Id}$. Se calcula:"),
                ("tex", r"f\bigl(f(x)\bigr)=\frac{2\cdot\frac{2x+1}{x-3}+1}{\frac{2x+1}{x-3}-3}"),
                ("md", "Numerador y denominador por separado:"),
                ("tex", r"\text{num: } \frac{2(2x+1)+(x-3)}{x-3}=\frac{4x+2+x-3}{x-3}=\frac{5x-1}{x-3}"),
                ("tex", r"\text{den: } \frac{(2x+1)-3(x-3)}{x-3}=\frac{2x+1-3x+9}{x-3}=\frac{-x+10}{x-3}"),
                ("tex", r"f\bigl(f(x)\bigr)=\frac{5x-1}{10-x}\ \neq\ x"),
                ("err", "**La afirmación de la diapositiva es incorrecta.** $f$ **no** es su propia "
                        "inversa: $f(f(x))=\\dfrac{5x-1}{10-x}$, no $x$. Verifíquese en $x=0$: "
                        "$f(0)=-\\tfrac13$ y $f(-\\tfrac13)=\\tfrac{1/3}{-10/3}=-\\tfrac{1}{10}$, "
                        "que no es $0$."),
                ("info", "Lo que sí es cierto: $f^{-1}$ tiene la **misma forma algebraica** "
                         "$\\dfrac{ax+b}{cx+d}$ que $f$. Eso vale para toda homografía, pero «misma "
                         "forma» no es «misma función». Un ejemplo real de involución es "
                         "$f(x)=\\dfrac{1}{x}$, o $f(x)=\\dfrac{x+1}{x-1}$."),
            ],
        },
        {
            "t": "Inversa con restricción de dominio",
            "f": "[D] diapositiva 61",
            "e": [("md", "Sea $f(x)=x^{2}-4x+5$ con $x\\ge2$. Hallar $f^{-1}$ y los dominios de ambas.")],
            "s": [
                ("md", "**Paso 1. Completar el cuadrado** (indispensable para poder despejar):"),
                ("tex", r"x^{2}-4x+5=(x^{2}-4x+4)+1=(x-2)^{2}+1"),
                ("md", "**Paso 2. Justificar la inyectividad.** Sobre $[2,\\infty)$ la expresión "
                       "$(x-2)^{2}$ es creciente (el argumento $x-2$ es $\\ge0$ y crece), así que $f$ es "
                       "creciente y por tanto inyectiva. El rango:"),
                ("tex", r"x\ge 2 \Rightarrow (x-2)^{2}\ge 0 \Rightarrow f(x)\ge 1 \qquad\Longrightarrow\qquad \operatorname{Ran}(f)=[1,+\infty)"),
                ("md", "**Paso 3. Despejar:**"),
                ("tex", r"y=(x-2)^{2}+1 \;\Longrightarrow\; (x-2)^{2}=y-1"),
                ("tex", r"x-2=\pm\sqrt{y-1}"),
                ("warn", "**Aquí se decide el signo con la restricción del dominio.** Como $x\\ge2$, se "
                         "tiene $x-2\\ge0$, así que se toma la raíz **positiva**. Si el dominio fuera "
                         "$x\\le2$, se tomaría la negativa y saldría otra inversa."),
                ("tex", r"x=2+\sqrt{y-1} \qquad\Longrightarrow\qquad f^{-1}(x)=2+\sqrt{x-1}"),
                ("md", "**Dominios:**"),
                ("tex", r"\operatorname{Dom}(f)=[2,+\infty)=\operatorname{Ran}(f^{-1}), \qquad \operatorname{Dom}(f^{-1})=[1,+\infty)=\operatorname{Ran}(f)"),
                ("md", "**Verificación en un punto:** $f(3)=9-12+5=2$, y "
                       "$f^{-1}(2)=2+\\sqrt{2-1}=2+1=3$ ✓"),
                ("fig", _fig_inv_cuadratica),
                ("info", "Sin la restricción $x\\ge2$ la parábola completa no es inyectiva "
                         "($f(1)=f(3)=2$) y no tendría inversa. Restringir el dominio es el "
                         "procedimiento estándar; es exactamente lo que se hace para definir "
                         "$\\arcsin$ y $\\arccos$."),
            ],
        },
        {
            "t": "Inversa de una función racional con raíz",
            "f": "[D] diapositiva 62(b)",
            "e": [("md", "Sea $g(x)=\\dfrac{1}{x^{2}+1}$ con $\\operatorname{Dom}(g)=[0,+\\infty)$. "
                         "Determinar si tiene inversa y hallarla.")],
            "s": [
                ("md", "**Inyectividad.** Para $x\\ge0$, al crecer $x$ crece $x^{2}+1$, y al crecer el "
                       "denominador **decrece** el cociente. Así $g$ es estrictamente decreciente en "
                       "$[0,\\infty)$, luego inyectiva. Sí tiene inversa."),
                ("md", "**Rango.** En $x=0$: $g(0)=1$ (valor máximo). Cuando $x\\to+\\infty$, "
                       "$g(x)\\to0^{+}$ sin alcanzarlo:"),
                ("tex", r"\operatorname{Ran}(g)=(0,1]"),
                ("md", "**Despeje.**"),
                ("tex", r"y=\frac{1}{x^{2}+1} \;\Longrightarrow\; y(x^{2}+1)=1 \;\Longrightarrow\; x^{2}+1=\frac{1}{y}"),
                ("tex", r"x^{2}=\frac{1}{y}-1=\frac{1-y}{y}"),
                ("md", "Como el dominio es $x\\ge0$, se toma la raíz positiva:"),
                ("tex", r"x=\sqrt{\frac{1-y}{y}} \qquad\Longrightarrow\qquad g^{-1}(x)=\sqrt{\frac{1-x}{x}}"),
                ("tex", r"\operatorname{Dom}(g^{-1})=(0,1]"),
                ("md", "**Coherencia del dominio de $g^{-1}$:** el radicando "
                       "$\\dfrac{1-x}{x}\\ge0$ se cumple justo para $0<x\\le1$, que es exactamente "
                       "$\\operatorname{Ran}(g)$. Las dos rutas dan lo mismo, buena señal."),
                ("md", "**Verificación:** $g(1)=\\tfrac12$, y "
                       "$g^{-1}\\!\\left(\\tfrac12\\right)=\\sqrt{\\tfrac{1/2}{1/2}}=\\sqrt1=1$ ✓"),
            ],
        },
        {
            "t": "Composición aplicada: área que crece con el tiempo",
            "f": "[D] diapositiva 54",
            "e": [("md", "El radio de un círculo crece según $r(t)=2t+1$ (cm, con $t$ en segundos) y el "
                         "área es $A(r)=\\pi r^{2}$.\n\n"
                         "(a) Expresar el área como función del tiempo.  \n"
                         "(b) Calcular el área a los 3 s.  \n"
                         "(c) ¿En qué instante el área es $100\\pi$ cm²?")],
            "s": [
                ("md", "**(a)** El área depende del radio y el radio del tiempo: hay que **encadenar**. "
                       "La composición correcta es $A\\circ r$, no $r\\circ A$ (no tiene sentido meter "
                       "un área en la fórmula del radio)."),
                ("tex", r"(A\circ r)(t)=A\bigl(r(t)\bigr)=\pi(2t+1)^{2}=\pi(4t^{2}+4t+1)"),
                ("md", "**(b)** En $t=3$:"),
                ("tex", r"(A\circ r)(3)=\pi(2\cdot 3+1)^{2}=\pi(7)^{2}=49\pi\approx 153.9\ \text{cm}^{2}"),
                ("md", "**(c)** Se plantea la ecuación y se resuelve:"),
                ("tex", r"\pi(2t+1)^{2}=100\pi \;\Longrightarrow\; (2t+1)^{2}=100"),
                ("tex", r"2t+1=\pm 10"),
                ("md", "La raíz $2t+1=-10$ da $t=-5.5$ s, que se **descarta** por no tener sentido "
                       "físico ($t\\ge0$). Queda:"),
                ("tex", r"2t+1=10 \;\Longrightarrow\; t=4.5\ \text{s}"),
                ("fig", _fig_area_tiempo),
                ("warn", "Descartar la raíz sin sentido físico es parte de la solución, no un detalle. "
                         "Hay que escribir **por qué** se descarta."),
                ("info", "El inciso (c) es en el fondo una **inversa**: se pregunta $t$ dado $A$, es "
                         "decir $(A\\circ r)^{-1}(100\\pi)$."),
            ],
        },
        {
            "t": "Inversa aplicada: temperatura de un horno",
            "f": "[D] diapositiva 63",
            "e": [("md", "La temperatura de un horno sube linealmente: $T(t)=25+8t$ (°C), "
                         "con $t\\in[0,30]$ min.\n\n"
                         "(a) Hallar $T^{-1}$ e interpretarla.  \n"
                         "(b) ¿En qué minuto se alcanzan 180 °C?  \n"
                         "(c) ¿Cuál es el rango de $T$?")],
            "s": [
                ("md", "**(a)** $T$ es lineal con pendiente $8>0$, así que es creciente e inyectiva; "
                       "tiene inversa. Despejando $t$:"),
                ("tex", r"T=25+8t \;\Longrightarrow\; T-25=8t \;\Longrightarrow\; t=\frac{T-25}{8}"),
                ("tex", r"T^{-1}(T)=\frac{T-25}{8}"),
                ("ok", "**Interpretación:** mientras $T(t)$ responde «¿qué temperatura hay al minuto "
                       "$t$?», la inversa $T^{-1}$ responde «¿en qué minuto se alcanza la temperatura "
                       "$T$?». Se invierten pregunta y respuesta, y también las **unidades**: "
                       "$T$ recibe minutos y devuelve °C; $T^{-1}$ recibe °C y devuelve minutos."),
                ("md", "**(b)**"),
                ("tex", r"T^{-1}(180)=\frac{180-25}{8}=\frac{155}{8}=19.375\approx 19.4\ \text{min}"),
                ("md", "**(c)** Como $T$ es creciente en $[0,30]$, el rango va del valor en el extremo "
                       "izquierdo al del derecho:"),
                ("tex", r"T(0)=25, \qquad T(30)=25+240=265"),
                ("tex", r"\operatorname{Ran}(T)=[25,265]\ \text{°C}"),
                ("md", "Y en consecuencia $\\operatorname{Dom}(T^{-1})=[25,265]$: sólo tiene sentido "
                       "preguntar por temperaturas que el horno realmente alcanza."),
                ("warn", "Preguntar $T^{-1}(300)$ daría $34.4$ min, fuera del intervalo válido. La "
                         "fórmula sigue calculando, pero el modelo ya no aplica: **siempre** hay que "
                         "revisar el dominio."),
            ],
        },
    ]
    mostrar_ejercicios(ejercicios_u4, abrir_todo)


# ==================================================================================
# TAB 5 — TIPOS Y FAMILIAS
# ==================================================================================
with TABS[5]:
    st.header("5 · Tipos y familias de funciones")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Forma de presentación")
        st.markdown(
            """
- **Explícita:** $y$ está despejada, $y=f(x)$. Ej.: $y=3x^{2}-5x+1$.
- **Implícita:** una ecuación $F(x,y)=0$ sin despejar. Ej.: $x^{2}+y^{2}=r^{2}$.
  Suele **no** ser función, pero se parte en **ramas** que sí lo son.
- **Paramétrica:** $x=x(t)$, $y=y(t)$ con $t$ en un intervalo.
- **Por tramos:** distintas reglas según la zona del dominio.
"""
        )
        st.markdown("#### Clasificación algebraica")
        st.markdown(
            """
| Familia | Forma | Dominio |
|---|---|---|
| Polinomial | $a_nx^n+\\dots+a_0$ | $\\mathbb{R}$ siempre |
| Racional | $\\dfrac{p(x)}{q(x)}$ | $\\{x : q(x)\\neq0\\}$ |
| Irracional | $\\sqrt[n]{g(x)}$ | $n$ par: $g(x)\\ge0$; $n$ impar: el de $g$ |
"""
        )
    with c2:
        st.markdown("#### Paridad")
        st.latex(r"f \text{ par} \iff f(-x)=f(x) \quad (\text{simetría respecto al eje } y)")
        st.latex(r"f \text{ impar} \iff f(-x)=-f(x) \quad (\text{simetría respecto al origen})")
        st.markdown(
            "**Cómo se prueba:** calcular $f(-x)$, simplificar y comparar con $f(x)$ y con $-f(x)$. "
            "Si no coincide con ninguna, no es par ni impar (que es el caso más común)."
        )
        st.info("Si $f$ es impar y $0\\in\\operatorname{Dom}(f)$, entonces $f(0)=0$.\n\n"
                "*Prueba:* $f(-0)=-f(0)$, pero $-0=0$, luego $f(0)=-f(0)$, es decir $2f(0)=0$.")
        st.markdown("#### Trigonométricas")
        st.markdown(
            """
| | $\\operatorname{sen}x$ | $\\cos x$ | $\\tan x$ |
|---|---|---|---|
| Dominio | $\\mathbb{R}$ | $\\mathbb{R}$ | $\\mathbb{R}\\setminus\\{\\tfrac{\\pi}{2}+n\\pi\\}$ |
| Rango | $[-1,1]$ | $[-1,1]$ | $\\mathbb{R}$ |
| Período | $2\\pi$ | $2\\pi$ | $\\pi$ |
| Paridad | impar | par | impar |
"""
        )
        st.latex(r"\operatorname{sen}^{2}x+\cos^{2}x=1")

    st.markdown("---")
    st.subheader("Ejemplos resueltos")

    def _fig_paridad():
        fig, axes = plt.subplots(1, 3, figsize=(9.5, 2.8))
        x = np.linspace(-2.2, 2.2, 400)
        axes[0].plot(x, x ** 4 - 3 * x ** 2 + 1, color=AZUL, lw=2)
        axes[0].set_title("Par: simétrica al eje $y$", fontsize=9, color=VERDE)
        axes[1].plot(x, x ** 5 - 3 * x, color=AZUL, lw=2)
        axes[1].plot([0], [0], "o", color=VERDE, ms=6)
        axes[1].set_title("Impar: simétrica al origen", fontsize=9, color=VERDE)
        axes[2].plot(x, x ** 2 + x, color=AZUL, lw=2)
        axes[2].set_title("Ni par ni impar", fontsize=9, color=ROJO)
        for a in axes:
            a.axhline(0, color="0.3", lw=0.8)
            a.axvline(0, color="0.3", lw=0.8)
            a.grid(alpha=0.2, ls=":")
        fig.tight_layout()
        return fig

    def _fig_tramos():
        fig, ax = nueva_fig()
        x1 = np.linspace(-2, 1, 200)
        x2 = np.linspace(1, 3, 200)
        ax.plot(x1, x1 ** 2, color=AZUL, lw=2)
        ax.plot(x2, 2 * x2 + 1, color=OCRE, lw=2)
        ax.plot([1], [1], "o", color=AZUL, ms=8)
        ax.plot([1], [3], "o", mfc="white", mec=OCRE, mew=2, ms=8)
        ax.annotate("lleno $(1,1)$", (1, 1), textcoords="offset points", xytext=(10, -16), fontsize=8)
        ax.annotate("hueco $(1,3)$", (1, 3), textcoords="offset points", xytext=(10, 4), fontsize=8)
        ax.set_title(r"$f(x)=x^{2}$ si $x\leq 1$;  $2x+1$ si $x>1$", fontsize=10)
        ax.set_ylim(-1, 8)
        fig.tight_layout()
        return fig

    ejemplos_u5 = [
        {
            "t": "Determinar paridad algebraicamente",
            "f": "[D] diapositivas 72–73",
            "c": [
                ("md", "Clasificar: (a) $f(x)=x^{4}-3x^{2}+1$  (b) $g(x)=x^{5}-3x$  (c) $h(x)=x^{2}+x$"),
                ("md", "**(a)** Se sustituye $-x$ y se simplifica usando que potencia **par** de "
                       "negativo es positiva:"),
                ("tex", r"f(-x)=(-x)^{4}-3(-x)^{2}+1=x^{4}-3x^{2}+1=f(x)"),
                ("ok", "**Par.** Regla rápida: polinomio con **todos** los exponentes pares (el término "
                       "constante cuenta como $x^0$, par)."),
                ("md", "**(b)** Potencia impar de negativo conserva el signo negativo:"),
                ("tex", r"g(-x)=(-x)^{5}-3(-x)=-x^{5}+3x=-\bigl(x^{5}-3x\bigr)=-g(x)"),
                ("ok", "**Impar.** Todos los exponentes impares. Nótese que $g(0)=0$, como debe ser."),
                ("md", "**(c)** Se mezclan exponentes:"),
                ("tex", r"h(-x)=(-x)^{2}+(-x)=x^{2}-x"),
                ("md", "Comparación: $h(x)=x^{2}+x$ y $-h(x)=-x^{2}-x$. El resultado $x^{2}-x$ no es "
                       "ninguno de los dos."),
                ("err", "**Ni par ni impar.** Contraejemplo explícito: $h(1)=2$ pero $h(-1)=0$; no es "
                        "ni $2$ (par) ni $-2$ (impar)."),
                ("fig", _fig_paridad),
                ("info", "La mayoría de las funciones no son ni pares ni impares. «Par» e «impar» "
                         "**no** son opciones complementarias."),
            ],
        },
        {
            "t": "Graficar una función definida por tramos",
            "f": "[S] Ejemplo 4, p. 155",
            "c": [
                ("md", "Graficar $f(x)=\\begin{cases}x^{2} & \\text{si } x\\le1\\\\ 2x+1 & \\text{si } x>1\\end{cases}$"),
                ("md", "**Procedimiento:** graficar cada pieza **sólo en su zona**, y marcar con "
                       "cuidado qué pasa en la frontera $x=1$."),
                ("md", "- Para $x\\le1$: la parábola $y=x^{2}$, pero recortada a la izquierda de $1$. "
                       "En $x=1$ vale $1$, y como la desigualdad **incluye** el igual, el punto "
                       "$(1,1)$ es **lleno**.\n"
                       "- Para $x>1$: la recta $y=2x+1$. En $x=1$ daría $3$, pero $x=1$ **no** "
                       "pertenece a este tramo, así que $(1,3)$ es un punto **hueco**."),
                ("fig", _fig_tramos),
                ("warn", "La convención de punto lleno / hueco no es decorativa: expresa a qué tramo "
                         "pertenece la frontera. Cada vertical corta la gráfica una sola vez, así que "
                         "sigue siendo función."),
                ("info", "El salto en $x=1$ (de altura $3-1=2$) es una **discontinuidad de salto**, "
                         "tema de la Unidad 2."),
            ],
        },
        {
            "t": "Función entero mayor (escalón)",
            "f": "[S] Ejemplo 6, p. 156",
            "c": [
                ("md", "Graficar $f(x)=\\lfloor x\\rfloor$ = el mayor entero menor o igual a $x$."),
                ("md", "**Valores de referencia:**"),
                ("tex", r"\lfloor 2\rfloor=2, \quad \lfloor 2.3\rfloor=2, \quad \lfloor 1.999\rfloor=1, \quad \lfloor -3.5\rfloor=-4, \quad \lfloor -0.5\rfloor=-1"),
                ("err", "Los negativos son la trampa: $\\lfloor-3.5\\rfloor=-4$, **no** $-3$. Se baja "
                        "al entero **menor o igual**, y $-3$ es mayor que $-3.5$."),
                ("md", "**Comportamiento:** entre dos enteros consecutivos la función es constante, así "
                       "que la gráfica son segmentos horizontales:"),
                ("md",
                 "| $x$ | $\\lfloor x\\rfloor$ |\n|---|---|\n"
                 "| $-2\\le x<-1$ | $-2$ |\n| $-1\\le x<0$ | $-1$ |\n"
                 "| $0\\le x<1$ | $0$ |\n| $1\\le x<2$ | $1$ |\n| $2\\le x<3$ | $2$ |"),

                ("fig", lambda: (
                    lambda fig_ax: (
                        [fig_ax[1].plot([n, n + 1], [n, n], color=AZUL, lw=2) for n in range(-3, 4)],
                        [fig_ax[1].plot([n], [n], "o", color=AZUL, ms=6) for n in range(-3, 4)],
                        [fig_ax[1].plot([n + 1], [n], "o", mfc="white", mec=AZUL, mew=1.6, ms=6)
                         for n in range(-3, 4)],
                        fig_ax[1].set_xlim(-3.5, 4.5),
                        fig_ax[1].set_ylim(-3.5, 4.5),
                        fig_ax[1].set_title(r"$y=\lfloor x\rfloor$", fontsize=10),
                        fig_ax[0].tight_layout(),
                    ) and fig_ax[0]
                )(nueva_fig())),
                ("info", "Cada escalón lleva punto **lleno** a la izquierda y **hueco** a la derecha. "
                         "Es el prototipo de **función escalón**, y modela cobros por unidad completa "
                         "(estacionamiento por hora, minutos de llamada)."),
            ],
        },
    ]
    mostrar_ejemplos(ejemplos_u5)

    st.markdown("---")
    st.subheader("Ejercicios")

    def _fig_racional():
        fig, ax = nueva_fig(figsize=(5.6, 3.6))
        for a, b in [(-4, -2.05), (-1.95, 1.95), (2.05, 4)]:
            x = np.linspace(a, b, 400)
            ax.plot(x, (x ** 2 - 1) / (x ** 2 - 4), color=AZUL, lw=2)
        ax.axvline(-2, color=ROJO, ls="--", lw=1.2)
        ax.axvline(2, color=ROJO, ls="--", lw=1.2)
        ax.axhline(1, color=VERDE, ls="--", lw=1.4)
        ax.plot([-1, 1], [0, 0], "o", color=OCRE, ms=7)
        ax.set_ylim(-6, 6)
        ax.set_title(r"$r(x)=\frac{x^{2}-1}{x^{2}-4}$   ·   AV en $x=\pm2$, AH en $y=1$", fontsize=9)
        fig.tight_layout()
        return fig

    def _fig_parametrica():
        fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2))
        t = np.linspace(0, 2 * np.pi, 400)
        axes[0].plot(np.cos(t), np.sin(t), color=AZUL, lw=2)
        axes[0].plot([1], [0], "o", color=OCRE, ms=7)
        axes[0].annotate("$t=0$", (1, 0), textcoords="offset points", xytext=(6, 6), fontsize=8)
        axes[0].set_title(r"$x=\cos t,\ y=\operatorname{sen} t$", fontsize=9)
        axes[0].set_aspect("equal")
        s = np.linspace(-2, 2, 300)
        axes[1].plot(s, s ** 2 - 1, color=AZUL, lw=2)
        axes[1].plot([-2, 2], [3, 3], "o", color=OCRE, ms=6)
        axes[1].set_title(r"$x=t,\ y=t^{2}-1,\ t\in[-2,2]$", fontsize=9)
        for a in axes:
            a.axhline(0, color="0.3", lw=0.8)
            a.axvline(0, color="0.3", lw=0.8)
            a.grid(alpha=0.2, ls=":")
        fig.tight_layout()
        return fig

    ejercicios_u5 = [
        {
            "t": "Clasificar paridad (batería)",
            "f": "[D] diapositivas 72–73",
            "e": [("md", "Determinar si cada función es par, impar o ninguna:\n\n"
                         "(a) $f(x)=|x|$  (b) $g(x)=\\dfrac{x}{x^{2}+1}$  (c) $h(x)=x\\operatorname{sen}x$  "
                         "(d) $p(x)=x^{3}+1$  (e) $q(x)=\\cos x + x^{2}$")],
            "s": [
                ("md", "**(a)** $f(-x)=|-x|=|x|=f(x)$ → **par**."),
                ("md", "**(b)** Numerador impar, denominador par:"),
                ("tex", r"g(-x)=\frac{-x}{(-x)^{2}+1}=\frac{-x}{x^{2}+1}=-g(x)"),
                ("md", "→ **impar**. (Y en efecto $g(0)=0$.)"),
                ("md", "**(c)** Producto de dos impares ($x$ y $\\operatorname{sen}x$):"),
                ("tex", r"h(-x)=(-x)\operatorname{sen}(-x)=(-x)(-\operatorname{sen}x)=x\operatorname{sen}x=h(x)"),
                ("md", "→ **par**."),
                ("ok", "**Reglas de producto:** par·par = par; impar·impar = **par**; par·impar = impar. "
                       "Se comportan como la suma de exponentes."),
                ("md", "**(d)** $p(-x)=-x^{3}+1$. No es $p(x)=x^3+1$ ni $-p(x)=-x^3-1$ → **ninguna**."),
                ("warn", "El $+1$ arruina la imparidad de $x^3$: rompe la simetría respecto al origen "
                         "porque $p(0)=1\\neq0$. Sumar una constante $\\neq0$ **destruye** la imparidad "
                         "pero **conserva** la paridad."),
                ("md", "**(e)** Suma de par ($\\cos x$) más par ($x^2$):"),
                ("tex", r"q(-x)=\cos(-x)+(-x)^{2}=\cos x+x^{2}=q(x)"),
                ("md", "→ **par**."),
            ],
        },
        {
            "t": "Dominio y rango de funciones irracionales",
            "f": "[D] diapositiva 71",
            "e": [("md", "Hallar dominio y rango de:\n\n"
                         "(a) $f(x)=\\sqrt{4-x^{2}}$  (b) $g(x)=\\sqrt[3]{x-1}$")],
            "s": [
                ("md", "**(a) Índice par** → radicando $\\ge0$."),
                ("tex", r"4-x^{2}\ge 0 \iff x^{2}\le 4 \iff -2\le x\le 2"),
                ("tex", r"\operatorname{Dom}(f)=[-2,2]"),
                ("md", "**Rango:** el radicando $4-x^2$ recorre $[0,4]$ en ese dominio (vale $0$ en los "
                       "extremos y $4$ en $x=0$). Como la raíz es creciente:"),
                ("tex", r"\operatorname{Ran}(f)=\left[\sqrt{0},\sqrt{4}\right]=[0,2]"),
                ("info", "Geométricamente $y=\\sqrt{4-x^2}$ equivale a $x^{2}+y^{2}=4$ con $y\\ge0$: es "
                         "el **semicírculo superior** de radio 2, que es una rama de la circunferencia."),
                ("md", "**(b) Índice impar** → **no hay restricción**. La raíz cúbica de un negativo "
                       "existe: $\\sqrt[3]{-8}=-2$."),
                ("tex", r"\operatorname{Dom}(g)=\mathbb{R}, \qquad \operatorname{Ran}(g)=\mathbb{R}"),
                ("err", "Error muy frecuente: aplicar «radicando $\\ge0$» a **toda** raíz. Sólo vale "
                        "para índice **par**."),
            ],
        },
        {
            "t": "Función racional: dominio, asíntotas y ceros",
            "f": "[D] diapositiva 70",
            "e": [("md", "Sea $r(x)=\\dfrac{x^{2}-1}{x^{2}-4}$. Hallar dominio, asíntotas verticales, "
                         "asíntota horizontal y ceros.")],
            "s": [
                ("md", "**Factorizar primero, siempre:**"),
                ("tex", r"r(x)=\frac{(x-1)(x+1)}{(x-2)(x+2)}"),
                ("md", "**Dominio:** ceros del denominador, $x=\\pm2$. No hay factores comunes que "
                       "cancelar, así que ambos son asíntotas y no huecos."),
                ("tex", r"\operatorname{Dom}(r)=\mathbb{R}\setminus\{-2,2\}"),
                ("md", "**Asíntotas verticales:** $x=-2$ y $x=2$."),
                ("md", "**Asíntota horizontal:** se comparan los grados. Numerador y denominador son "
                       "ambos de grado 2, así que la asíntota es el cociente de los coeficientes "
                       "principales, $1/1$:"),
                ("tex", r"y=1"),
                ("md", "Se puede ver dividiendo entre $x^{2}$:"),
                ("tex", r"r(x)=\frac{1-\frac{1}{x^{2}}}{1-\frac{4}{x^{2}}} \xrightarrow[\ |x|\to\infty\ ]{} \frac{1-0}{1-0}=1"),
                ("md", "**Ceros:** donde el numerador se anula (y el denominador no): $x=\\pm1$."),
                ("fig", _fig_racional),
                ("info", "**Regla de grados para la asíntota horizontal:** grado num < grado den → "
                         "$y=0$; grados iguales → cociente de coeficientes principales; grado num > "
                         "grado den → no hay AH (puede haber oblicua)."),
            ],
        },
        {
            "t": "De implícita a explícita: ramas",
            "f": "[D] diapositiva 66",
            "e": [("md", "La ecuación $x^{2}+y^{2}=9$ define una circunferencia.\n\n"
                         "(a) ¿Define $y$ como función de $x$?  \n"
                         "(b) Escribir las ramas que sí son funciones, con dominio y rango.")],
            "s": [
                ("md", "**(a)** No. Al despejar:"),
                ("tex", r"y^{2}=9-x^{2} \;\Longrightarrow\; y=\pm\sqrt{9-x^{2}}"),
                ("md", "El $\\pm$ es la señal: para $x=0$ hay dos valores, $y=3$ y $y=-3$. La vertical "
                       "$x=0$ corta dos veces, falla la prueba de la línea vertical."),
                ("md", "**(b)** Cada signo da una función:"),
                ("tex", r"y_{1}(x)=\sqrt{9-x^{2}} \quad \text{(semicírculo superior)}"),
                ("tex", r"y_{2}(x)=-\sqrt{9-x^{2}} \quad \text{(semicírculo inferior)}"),
                ("md", "Ambas tienen el mismo dominio, $9-x^{2}\\ge0 \\iff -3\\le x\\le3$:"),
                ("tex", r"\operatorname{Dom}(y_{1})=\operatorname{Dom}(y_{2})=[-3,3]"),
                ("tex", r"\operatorname{Ran}(y_{1})=[0,3], \qquad \operatorname{Ran}(y_{2})=[-3,0]"),
                ("md", "La unión de las gráficas reconstruye la circunferencia completa."),
                ("info", "Esta separación en ramas es la razón por la que en cálculo se inventa la "
                         "**derivación implícita**: permite trabajar con $x^2+y^2=9$ sin tener que "
                         "elegir rama."),
            ],
        },
        {
            "t": "Eliminar el parámetro",
            "f": "[D] diapositiva 67",
            "e": [("md", "Identificar la curva y el efecto del intervalo del parámetro:\n\n"
                         "(a) $x(t)=\\cos t$, $y(t)=\\operatorname{sen}t$, $t\\in[0,2\\pi]$  \n"
                         "(b) $x(t)=t$, $y(t)=t^{2}-1$, $t\\in[-2,2]$")],
            "s": [
                ("md", "**(a)** Se busca una relación entre $x$ e $y$ sin $t$. Aquí la clave es la "
                       "identidad pitagórica:"),
                ("tex", r"x^{2}+y^{2}=\cos^{2}t+\operatorname{sen}^{2}t=1"),
                ("md", "Es la circunferencia unitaria. Con $t\\in[0,2\\pi]$ se recorre **completa** y "
                       "exactamente una vez, empezando en $(1,0)$ y en sentido antihorario."),
                ("md", "**(b)** Como $x=t$, se sustituye directamente:"),
                ("tex", r"y=t^{2}-1=x^{2}-1"),
                ("md", "Es una parábola. Pero $t\\in[-2,2]$ y $x=t$, así que:"),
                ("tex", r"x\in[-2,2] \qquad\Longrightarrow\qquad y\in[-1,3]"),
                ("fig", _fig_parametrica),
                ("warn", "**El intervalo del parámetro es parte de la curva.** No es la parábola "
                         "completa: es sólo el **arco** entre $(-2,3)$ y $(2,3)$. Eliminar $t$ sin "
                         "arrastrar el rango de $x$ es el error típico."),
                ("info", "Ventaja de la forma paramétrica: describe curvas que **no** son funciones "
                         "(como la circunferencia) sin partirlas en ramas, y además codifica el "
                         "**sentido y la rapidez** del recorrido."),
            ],
        },
        {
            "t": "Función escalón aplicada: costo de una llamada",
            "f": "[S] Ejemplo 7, p. 156",
            "e": [("md", "Una llamada de larga distancia cuesta 69 centavos el primer minuto y 58 "
                         "centavos por cada minuto adicional **o fracción**. Expresar el costo $C$ "
                         "(en dólares) como función del tiempo $t$ (en minutos) y evaluar en "
                         "$t=0.5$, $t=1$, $t=1.2$ y $t=3$.")],
            "s": [
                ("md", "**Lo esencial: «o fracción».** Un segundo del minuto 2 ya cobra el minuto 2 "
                       "completo. El costo es constante dentro de cada minuto y salta al cruzarlo."),
                ("md", "Por tramos:"),
                ("tex", r"C(t)=\begin{cases} 0.69 & 0<t\le 1\\ 1.27 & 1<t\le 2\\ 1.85 & 2<t\le 3\\ \ \vdots \end{cases}"),
                ("md", "Forma compacta: si $n-1<t\\le n$ con $n$ entero positivo,"),
                ("tex", r"C(t)=0.69+0.58\,(n-1)"),
                ("md", "**Evaluaciones:**"),
                ("md", "- $t=0.5$: está en $(0,1]$ → $C=0.69$\n"
                       "- $t=1$: sigue en $(0,1]$ (el intervalo **cierra** en 1) → $C=0.69$\n"
                       "- $t=1.2$: está en $(1,2]$ → $C=0.69+0.58=1.27$\n"
                       "- $t=3$: está en $(2,3]$ → $C=0.69+2(0.58)=1.85$"),
                ("warn", "Los extremos importan: a $t=1$ exacto todavía se paga el mínimo; a $t=1.01$ "
                         "ya se paga el segundo minuto. Los intervalos son **abiertos por izquierda y "
                         "cerrados por derecha**, al revés que en $\\lfloor x\\rfloor$."),
                ("info", "Emparentada con la función entero mayor: aquí conviene la función **techo**, "
                         "$C(t)=0.69+0.58(\\lceil t\\rceil-1)$ para $t>0$."),
            ],
        },
        {
            "t": "Trigonométricas inversas: identidades de cancelación",
            "f": "[D] diapositiva 76",
            "e": [("md", "Calcular exactamente:\n\n"
                         "(a) $\\arcsin\\!\\left(\\operatorname{sen}\\dfrac{\\pi}{6}\\right)$  \n"
                         "(b) $\\arcsin\\!\\left(\\operatorname{sen}\\dfrac{5\\pi}{6}\\right)$  \n"
                         "(c) $\\cos\\!\\left(\\arcsin\\dfrac{3}{5}\\right)$")],
            "s": [
                ("md", "**Recordar los rangos restringidos** (sin ellos no habría inversa):"),
                ("tex", r"\arcsin\colon[-1,1]\to\left[-\tfrac{\pi}{2},\tfrac{\pi}{2}\right], \qquad \arccos\colon[-1,1]\to[0,\pi]"),
                ("md", "**(a)** Como $\\tfrac{\\pi}{6}$ **sí** está en $\\left[-\\tfrac{\\pi}{2},"
                       "\\tfrac{\\pi}{2}\\right]$, la cancelación es directa:"),
                ("tex", r"\arcsin\!\left(\operatorname{sen}\tfrac{\pi}{6}\right)=\tfrac{\pi}{6}"),
                ("md", "**(b)** Ahora $\\tfrac{5\\pi}{6}$ **no** está en ese intervalo, así que "
                       "**no se puede cancelar**. Hay que evaluar por dentro:"),
                ("tex", r"\operatorname{sen}\tfrac{5\pi}{6}=\tfrac{1}{2}"),
                ("tex", r"\arcsin\!\left(\tfrac{1}{2}\right)=\tfrac{\pi}{6}"),
                ("err", "**La respuesta es $\\tfrac{\\pi}{6}$, no $\\tfrac{5\\pi}{6}$.** La identidad "
                        "$\\arcsin(\\operatorname{sen}x)=x$ vale **sólo** para "
                        "$x\\in\\left[-\\tfrac{\\pi}{2},\\tfrac{\\pi}{2}\\right]$."),
                ("md", "**(c)** Sea $\\theta=\\arcsin\\tfrac35$, es decir "
                       "$\\operatorname{sen}\\theta=\\tfrac35$ con "
                       "$\\theta\\in\\left[-\\tfrac{\\pi}{2},\\tfrac{\\pi}{2}\\right]$. Por la "
                       "identidad pitagórica:"),
                ("tex", r"\cos^{2}\theta=1-\operatorname{sen}^{2}\theta=1-\tfrac{9}{25}=\tfrac{16}{25}"),
                ("tex", r"\cos\theta=\pm\tfrac{4}{5}"),
                ("md", "En ese intervalo el coseno es **no negativo**, así que se toma el signo positivo:"),
                ("tex", r"\cos\!\left(\arcsin\tfrac{3}{5}\right)=\tfrac{4}{5}"),
                ("info", "Truco visual para (c): triángulo rectángulo con cateto opuesto 3 e hipotenusa "
                         "5; el cateto adyacente es 4 (terna 3-4-5)."),
            ],
        },
    ]
    mostrar_ejercicios(ejercicios_u5, abrir_todo)


# ==================================================================================
# TAB 6 — MODELOS
# ==================================================================================
with TABS[6]:
    st.header("6 · Modelos matemáticos")

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("#### El proceso")
        st.markdown(
            """
1. **Identificar variables**: cuál es independiente y cuál dependiente.
2. **Recopilar datos** o invocar la ley física/geométrica que relaciona.
3. **Proponer** la función $y=f(x)$.
4. **Determinar el dominio con sentido físico** (casi nunca es el algebraico).
5. **Resolver** y **validar** contra casos conocidos.
6. **Interpretar** el resultado con unidades y en el contexto.
"""
        )
        st.warning(
            "**El paso 4 es el que más se olvida.** Un modelo casi siempre tiene un dominio menor "
            "que el de su fórmula: no hay tiempos negativos, ni radios negativos, ni cantidades "
            "producidas fraccionarias."
        )
    with c2:
        st.markdown("#### Herramientas recurrentes")
        st.markdown(
            """
- **Restricción geométrica** para eliminar una variable (Pitágoras, semejanza, volumen fijo).
- **Composición** cuando una cantidad depende de otra que a su vez depende del tiempo.
- **Inversa** cuando la pregunta invierte el papel de dato e incógnita
  («¿cuándo se alcanza...?» en vez de «¿cuánto vale en...?»).
- **Función por tramos** para tarifas, impuestos y escalas.
"""
        )
        st.success(
            "**Validación rápida:** revisar los valores en los extremos del dominio. Si $V(20)$ "
            "no da tanque vacío cuando el enunciado dice que se vacía en 20 min, el modelo está mal."
        )

    st.markdown("---")
    st.subheader("Ejemplos resueltos")

    def _fig_rectangulo():
        fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.2))
        R = 5
        x = np.linspace(0.001, R - 0.001, 400)
        A = 2 * x * np.sqrt(R ** 2 - x ** 2)
        axes[0].plot(x, A, color=AZUL, lw=2)
        axes[0].axhline(25, color=OCRE, ls="--")
        axes[0].plot([R / np.sqrt(2)], [25], "o", color=OCRE, ms=8)
        axes[0].set_title(r"$A(x)=2x\sqrt{25-x^{2}}$   máx $=25$ en $x=\frac{5}{\sqrt2}$", fontsize=9)
        axes[0].set_xlabel("x")
        axes[0].set_ylabel("A")
        axes[0].grid(alpha=0.25, ls=":")
        th = np.linspace(0, np.pi, 200)
        axes[1].plot(R * np.cos(th), R * np.sin(th), color=AZUL, lw=2)
        axes[1].plot([-R, R], [0, 0], color=AZUL, lw=2)
        xr = R / np.sqrt(2)
        hr = np.sqrt(R ** 2 - xr ** 2)
        axes[1].add_patch(plt.Rectangle((-xr, 0), 2 * xr, hr, fill=False, ec=VERDE, lw=2))
        axes[1].plot([0, xr], [0, hr], ls="--", color="0.5")
        axes[1].annotate("R", (xr / 2, hr / 2), fontsize=9, color="0.4")
        axes[1].annotate("h", (xr + 0.15, hr / 2), fontsize=9, color=VERDE)
        axes[1].annotate("x", (xr / 2, -0.5), fontsize=9, color=VERDE)
        axes[1].set_aspect("equal")
        axes[1].axis("off")
        axes[1].set_title("Rectángulo inscrito", fontsize=9)
        fig.tight_layout()
        return fig

    def _fig_caida():
        fig, ax = nueva_fig(xlabel="t (s)", ylabel="h (m)")
        t = np.linspace(0, 3.03, 300)
        ax.plot(t, 45 - 4.9 * t ** 2, color=AZUL, lw=2)
        ax.plot([3.0304], [0], "o", color=OCRE, ms=8)
        ax.annotate(r"$t^{*}\approx 3.03$ s", (3.03, 0), textcoords="offset points",
                    xytext=(-70, 14), color=OCRE)
        ax.set_xlim(0, 3.6)
        ax.set_ylim(0, 50)
        ax.set_title(r"$h(t)=45-4.9t^{2}$", fontsize=10)
        fig.tight_layout()
        return fig

    ejemplos_u6 = [
        {
            "t": "Modelo geométrico: rectángulo inscrito en un semicírculo",
            "f": "[D] diapositiva 79",
            "c": [
                ("md", "Un rectángulo está inscrito en un semicírculo de radio $R$, con la base sobre "
                       "el diámetro. Expresar el área como función de la mitad de la base, $x$."),
                ("md", "**Paso 1. Variables.** Sea $x$ = mitad de la base (así la base es $2x$) y $h$ = "
                       "altura. El área es $A=(\\text{base})(\\text{altura})=2xh$: **dos** incógnitas, "
                       "hace falta eliminar una."),
                ("md", "**Paso 2. Restricción geométrica.** El vértice superior derecho está **sobre** "
                       "el semicírculo, así que sus coordenadas $(x,h)$ satisfacen la ecuación de la "
                       "circunferencia:"),
                ("tex", r"x^{2}+h^{2}=R^{2} \;\Longrightarrow\; h=\sqrt{R^{2}-x^{2}}"),
                ("md", "(se toma la raíz positiva porque $h$ es una altura)."),
                ("md", "**Paso 3. Sustituir** para quedarse con una sola variable:"),
                ("tex", r"A(x)=2x\sqrt{R^{2}-x^{2}}, \qquad x\in(0,R)"),
                ("md", "**Paso 4. Dominio físico.** Con $x=0$ o $x=R$ el rectángulo degenera (área "
                       "cero), así que el intervalo abierto $(0,R)$ es lo razonable."),
                ("md", "**Caso $R=5$.** El máximo se alcanza en $x=\\dfrac{R}{\\sqrt2}\\approx3.54$:"),
                ("tex", r"A\!\left(\tfrac{5}{\sqrt{2}}\right)=2\cdot\tfrac{5}{\sqrt{2}}\cdot\sqrt{25-\tfrac{25}{2}}=2\cdot\tfrac{5}{\sqrt{2}}\cdot\tfrac{5}{\sqrt{2}}=\tfrac{50}{2}=25"),
                ("fig", _fig_rectangulo),
                ("ok", "El área máxima es $R^{2}=25$ (exactamente la mitad del cuadrado de lado $R\\sqrt2$). "
                       "En cálculo esto se obtendrá con $A'(x)=0$; aquí basta la gráfica."),
                ("info", "**La técnica es siempre la misma:** escribir la cantidad de interés, notar "
                         "que tiene dos variables, y usar la restricción geométrica para eliminar una."),
            ],
        },
        {
            "t": "Modelo físico: caída libre",
            "f": "[D] diapositiva 80",
            "c": [
                ("md", "Un objeto cae desde el reposo desde $h_0=45$ m. Con $g=9.8$ m/s²:"),
                ("tex", r"h(t)=45-4.9\,t^{2}, \qquad v(t)=9.8\,t"),
                ("md", "**(a) ¿Cuándo llega al suelo?** Llegar al suelo significa $h=0$:"),
                ("tex", r"45-4.9t^{2}=0 \;\Longrightarrow\; t^{2}=\frac{45}{4.9}\approx 9.184"),
                ("tex", r"t^{*}=\sqrt{9.184}\approx 3.03\ \text{s}"),
                ("md", "(se descarta la raíz negativa $t\\approx-3.03$ por carecer de sentido físico)."),
                ("md", "**(b) Velocidad de impacto:**"),
                ("tex", r"v(3.03)=9.8\times 3.03\approx 29.7\ \text{m/s} \approx 107\ \text{km/h}"),
                ("fig", _fig_caida),
                ("warn", "**Dominio del modelo:** $t\\in[0,\\;3.03]$. Para $t=5$ la fórmula daría "
                         "$h=45-122.5=-77.5$ m, es decir 77 metros bajo tierra. La fórmula sigue "
                         "calculando; el modelo ya no describe nada."),
                ("info", "Compárese con el $d(t)=16t^{2}$ (en pies) del inicio del capítulo 2 de "
                         "Stewart: es la misma ley de Galileo en otras unidades."),
            ],
        },
        {
            "t": "Modelo económico: ingreso, costo y utilidad",
            "f": "[D] diapositiva 81",
            "c": [
                ("md", "Costo total $C(q)=0.01q^{2}+5q+200$ y precio unitario $p(q)=50-0.1q$. "
                       "Hallar ingreso, utilidad y puntos de equilibrio."),
                ("md", "**Ingreso** = precio × cantidad (ojo: el precio **depende** de $q$):"),
                ("tex", r"I(q)=p(q)\cdot q=(50-0.1q)\,q=50q-0.1q^{2}"),
                ("md", "**Utilidad** = ingreso − costo:"),
                ("tex", r"U(q)=I(q)-C(q)=\bigl(50q-0.1q^{2}\bigr)-\bigl(0.01q^{2}+5q+200\bigr)"),
                ("tex", r"U(q)=45q-0.11q^{2}-200"),
                ("md", "**Puntos de equilibrio** ($U=0$, no se gana ni se pierde):"),
                ("tex", r"0.11q^{2}-45q+200=0"),
                ("tex", r"q=\frac{45\pm\sqrt{45^{2}-4(0.11)(200)}}{2(0.11)}=\frac{45\pm\sqrt{1937}}{0.22}"),
                ("tex", r"q\approx 4.5 \quad \text{o} \quad q\approx 405\ \text{unidades}"),
                ("md", "**Interpretación:** se gana dinero **entre** esos dos valores. Por debajo de 5 "
                       "unidades no se cubren los \\$200 de costo fijo; por arriba de 405 el precio ha "
                       "caído tanto (por $p=50-0.1q$) que producir más ya no compensa."),
                ("ok", "La utilidad máxima está en el vértice de la parábola, "
                       "$q=\\dfrac{45}{0.22}\\approx 205$ unidades, con $U\\approx 4404$."),
                ("warn", "$q$ debería ser entero (no se venden 4.5 unidades). El dominio con sentido "
                         "es $q\\in\\{0,1,2,\\dots\\}$; se trabaja con reales por comodidad y se "
                         "redondea al final."),
            ],
        },
    ]
    mostrar_ejemplos(ejemplos_u6)

    st.markdown("---")
    st.subheader("Ejercicios")

    def _fig_flujo():
        fig, ax = nueva_fig(xlabel="r (cm)", ylabel="v (cm/s)")
        r = np.linspace(0, 0.5, 200)
        ax.plot(r, 18500 * (0.25 - r ** 2), color=AZUL, lw=2)
        ax.plot([0], [4625], "o", color=OCRE, ms=7)
        ax.annotate("máx en el centro", (0, 4625), textcoords="offset points",
                    xytext=(14, -6), fontsize=8, color=OCRE)
        ax.set_xlim(-0.02, 0.55)
        ax.set_title("Ley de flujo laminar", fontsize=10)
        fig.tight_layout()
        return fig

    ejercicios_u6 = [
        {
            "t": "Costo de producción",
            "f": "[S] Ejercicio 69, p. 150",
            "e": [
                ("md", "El costo $C$ en dólares de producir $x$ yardas de tela es"),
                ("tex", r"C(x)=1500+3x+0.02x^{2}+0.0001x^{3}"),
                ("md", "(a) Hallar $C(10)$ y $C(100)$.  (b) Interpretar.  (c) Hallar $C(0)$."),
            ],
            "s": [
                ("md", "**(a)** Sustitución término a término, con cuidado en las potencias:"),
                ("tex", r"C(10)=1500+3(10)+0.02(100)+0.0001(1000)"),
                ("tex", r"C(10)=1500+30+2+0.1=1532.10"),
                ("tex", r"C(100)=1500+3(100)+0.02(10\,000)+0.0001(1\,000\,000)"),
                ("tex", r"C(100)=1500+300+200+100=2100"),
                ("md", "**(b)** $C(10)=\\$1532.10$ es el costo total de producir 10 yardas, y "
                       "$C(100)=\\$2100$ el de producir 100 yardas."),
                ("md", "**(c)**"),
                ("tex", r"C(0)=1500"),
                ("ok", "$C(0)=\\$1500$ son los **costos fijos**: se pagan aunque no se produzca nada "
                       "(renta, maquinaria, seguros)."),
                ("info", "**Observación económica:** producir 10 yardas cuesta \\$1532.10, o sea "
                         "\\$153.21 por yarda; producir 100 cuesta \\$2100, o sea \\$21 por yarda. "
                         "El costo fijo se reparte entre más unidades: **economía de escala**. "
                         "Pero el término $0.0001x^{3}$ crece rápido y eventualmente revierte la ventaja."),
            ],
        },
        {
            "t": "Área de una esfera",
            "f": "[S] Ejercicio 70, p. 151",
            "e": [("md", "El área superficial de una esfera es $S(r)=4\\pi r^{2}$.\n\n"
                         "(a) Hallar $S(2)$ y $S(3)$.  (b) Interpretar.")],
            "s": [
                ("tex", r"S(2)=4\pi(2)^{2}=16\pi\approx 50.27"),
                ("tex", r"S(3)=4\pi(3)^{2}=36\pi\approx 113.10"),
                ("md", "**(b)** Son las áreas superficiales de esferas de radio 2 y 3 (en unidades "
                       "cuadradas: si $r$ está en cm, $S$ está en cm²)."),
                ("ok", "**Lo interesante:** el radio creció un 50 % ($2\\to3$) pero el área creció "
                       "$\\dfrac{36\\pi}{16\\pi}=2.25$ veces, es decir $(1.5)^{2}$. En una función "
                       "cuadrática, escalar la entrada por $k$ escala la salida por $k^{2}$."),
                ("md", "**Dominio con sentido físico:** $r>0$, aunque la fórmula acepte cualquier real. "
                       "No existen esferas de radio negativo."),
                ("info", "Enlaza con el error del inicio: $S(2r)=4\\pi(2r)^2=16\\pi r^2=4S(r)$, "
                         "**no** $2S(r)$."),
            ],
        },
        {
            "t": "¿A qué distancia puede usted ver?",
            "f": "[S] Ejercicio 72, p. 151",
            "e": [
                ("md", "Por la curvatura de la Tierra, la distancia máxima $D$ visible desde una "
                       "altitud $h$ es"),
                ("tex", r"D(h)=\sqrt{2rh+h^{2}}, \qquad r=3960 \text{ millas}"),
                ("md", "(a) Hallar $D(0.1)$ y $D(0.2)$.  \n"
                       "(b) ¿Qué distancia se ve desde la Torre CN, a 1135 pies?  \n"
                       "(c) ¿Y desde un avión a 7 millas?"),
            ],
            "s": [
                ("md", "**(a)** Con $h$ en millas:"),
                ("tex", r"D(0.1)=\sqrt{2(3960)(0.1)+(0.1)^{2}}=\sqrt{792+0.01}\approx 28.1 \text{ mi}"),
                ("tex", r"D(0.2)=\sqrt{2(3960)(0.2)+(0.2)^{2}}=\sqrt{1584+0.04}\approx 39.8 \text{ mi}"),
                ("warn", "**Conversión obligatoria en (b).** Los datos deben estar en las mismas "
                         "unidades que $r$. Como 1 milla = 5280 pies:"),
                ("tex", r"h=\frac{1135}{5280}\approx 0.2150 \text{ millas}"),
                ("tex", r"D\approx\sqrt{2(3960)(0.2150)+(0.2150)^{2}}=\sqrt{1702.5+0.046}\approx 41.3 \text{ mi}"),
                ("md", "**(c)** Con $h=7$ millas:"),
                ("tex", r"D(7)=\sqrt{2(3960)(7)+49}=\sqrt{55\,440+49}=\sqrt{55\,489}\approx 235.6 \text{ mi}"),
                ("ok", "**Observación estructural:** cuando $h$ es pequeña frente a $r$, el término "
                       "$h^{2}$ es despreciable y $D\\approx\\sqrt{2rh}$: la distancia crece como la "
                       "**raíz** de la altura. Duplicar la altura sólo multiplica el alcance por "
                       "$\\sqrt2\\approx1.41$, no por 2."),
                ("info", "Verificación de coherencia con (a): $D(0.2)/D(0.1)=39.8/28.1\\approx1.42\\approx\\sqrt2$ ✓"),
            ],
        },
        {
            "t": "Ley de flujo laminar",
            "f": "[S] Ejercicio 73, p. 151",
            "e": [
                ("md", "Para una arteria de radio 0.5 cm, la velocidad de la sangre a distancia $r$ "
                       "del eje central es"),
                ("tex", r"v(r)=18\,500\,(0.25-r^{2}), \qquad 0\le r\le 0.5"),
                ("md", "(a) Hallar $v(0.1)$ y $v(0.4)$.  (b) Interpretar.  (c) Tabular."),
            ],
            "s": [
                ("md", "**(a)**"),
                ("tex", r"v(0.1)=18\,500\,(0.25-0.01)=18\,500(0.24)=4440 \text{ cm/s}"),
                ("tex", r"v(0.4)=18\,500\,(0.25-0.16)=18\,500(0.09)=1665 \text{ cm/s}"),
                ("md", "**(b)** Cerca del eje ($r=0.1$) la sangre fluye mucho más rápido que cerca de "
                       "la pared ($r=0.4$): unas 2.7 veces más. La fricción con la pared frena el flujo."),
                ("md", "**(c) Tabla:**"),
                ("md",
                 "| $r$ (cm) | $0.25-r^2$ | $v(r)$ (cm/s) |\n|---|---|---|\n"
                 "| 0.0 | 0.25 | 4625 |\n| 0.1 | 0.24 | 4440 |\n| 0.2 | 0.21 | 3885 |\n"
                 "| 0.3 | 0.16 | 2960 |\n| 0.4 | 0.09 | 1665 |\n| 0.5 | 0.00 | 0 |"),
                ("fig", _fig_flujo),
                ("ok", "**Validación del modelo:** $v(0.5)=0$, la sangre en contacto con la pared está "
                       "en reposo. Es exactamente la condición física de no deslizamiento, y el modelo "
                       "la reproduce. Buena señal de que la fórmula es correcta."),
                ("md", "**Dominio:** $[0,\\;0.5]$ y no más: $r$ no puede exceder el radio de la arteria, "
                       "y valores mayores darían velocidades negativas, sin sentido."),
            ],
        },
        {
            "t": "Impuesto sobre la renta (modelo por tramos)",
            "f": "[S] Ejercicio 76, p. 151",
            "e": [
                ("md", "En cierto país el impuesto $T$ sobre un ingreso $x$ es"),
                ("tex", r"T(x)=\begin{cases} 0 & \text{si } 0\le x\le 10\,000\\ 0.08x & \text{si } 10\,000<x\le 20\,000\\ 1600+0.15x & \text{si } 20\,000<x \end{cases}"),
                ("md", "(a) Hallar $T(5000)$, $T(12\\,000)$ y $T(25\\,000)$.  (b) Interpretar."),
            ],
            "s": [
                ("md", "**(a)** Primero identificar el tramo, después aplicar la fórmula."),
                ("md", "- $5000\\in[0,10\\,000]$ → primer tramo:"),
                ("tex", r"T(5000)=0"),
                ("md", "- $12\\,000\\in(10\\,000,20\\,000]$ → segundo tramo:"),
                ("tex", r"T(12\,000)=0.08(12\,000)=960"),
                ("md", "- $25\\,000>20\\,000$ → tercer tramo:"),
                ("tex", r"T(25\,000)=1600+0.15(25\,000)=1600+3750=5350"),
                ("md", "**(b)** Quien gana \\$5000 no paga impuesto (está bajo el umbral exento). "
                       "Quien gana \\$12\\,000 paga \\$960. Quien gana \\$25\\,000 paga \\$5350."),
                ("md", "**Tasas efectivas** (impuesto ÷ ingreso), que es lo que realmente compara:"),
                ("md",
                 "| Ingreso | Impuesto | Tasa efectiva |\n|---|---|---|\n"
                 "| \\$5 000 | \\$0 | 0 % |\n| \\$12 000 | \\$960 | 8.0 % |\n"
                 "| \\$25 000 | \\$5 350 | 21.4 % |"),
                ("ok", "Es un impuesto **progresivo**: a mayor ingreso, mayor proporción pagada."),
                ("warn", "Este modelo tiene una discontinuidad fea en $x=20\\,000$: por izquierda "
                         "$0.08(20\\,000)=1600$, por derecha $1600+0.15(20\\,000)=4600$. Ganar un peso "
                         "más dispararía el impuesto \\$3000. Los sistemas fiscales reales aplican la "
                         "tasa sólo al **excedente** para evitarlo, lo que los hace continuos."),
            ],
        },
        {
            "t": "Costo de una estancia en hotel (construir el modelo)",
            "f": "[S] Ejercicio 78, pp. 151–152",
            "e": [("md", "Una cadena hotelera cobra \\$75 por noche las primeras dos noches y \\$50 "
                         "por cada noche adicional.\n\n"
                         "(a) Escribir $T(x)$, el costo total por $x$ noches, como función por tramos.  \n"
                         "(b) Hallar $T(2)$, $T(3)$ y $T(5)$.  (c) Interpretar.")],
            "s": [
                ("md", "**(a)** Hay dos regímenes."),
                ("md", "*Primeras dos noches:* cada una cuesta \\$75, así que para $x\\le2$ el costo "
                       "es $75x$."),
                ("md", "*Noches adicionales:* si $x>2$, se pagan las dos primeras completas "
                       "($2\\times75=150$) más $(x-2)$ noches a \\$50:"),
                ("tex", r"T(x)=\begin{cases} 75x & \text{si } 0\le x\le 2\\[4pt] 150+50(x-2) & \text{si } x>2 \end{cases}"),
                ("md", "El segundo tramo se puede simplificar:"),
                ("tex", r"150+50(x-2)=150+50x-100=50x+50"),
                ("md", "**(b)**"),
                ("md", "- $T(2)=75(2)=150$\n"
                       "- $T(3)=50(3)+50=200$  (o bien $150+50=200$)\n"
                       "- $T(5)=50(5)+50=300$  (o bien $150+3\\times50=300$)"),
                ("md", "**(c)** Dos noches cuestan \\$150, tres \\$200 y cinco \\$300."),
                ("ok", "**Verificación de continuidad en $x=2$:** por el primer tramo $75(2)=150$; "
                       "por el segundo $50(2)+50=150$. **Coinciden**, así que no hay salto. A "
                       "diferencia del impuesto del ejercicio anterior, aquí el modelo es continuo "
                       "y no premia ni castiga cruzar la frontera."),
                ("info", "Esa verificación en la frontera debería hacerse **siempre** al construir un "
                         "modelo por tramos: detecta errores de planteamiento de inmediato."),
            ],
        },
        {
            "t": "Modelo con composición: globo que se infla",
            "f": "estilo [S] Enfoque sobre modelado",
            "e": [("md", "Un globo esférico se infla de modo que su radio crece a razón constante de "
                         "2 cm/s, partiendo de $r=0$.\n\n"
                         "(a) Expresar el radio como función del tiempo.  \n"
                         "(b) Expresar el **volumen** como función del tiempo.  \n"
                         "(c) ¿En qué instante el volumen es $288\\pi$ cm³?")],
            "s": [
                ("md", "**(a)** Rapidez constante ⇒ relación lineal:"),
                ("tex", r"r(t)=2t \quad \text{(cm, con } t \text{ en s)}"),
                ("md", "**(b)** El volumen de una esfera es $V(r)=\\dfrac{4}{3}\\pi r^{3}$. El volumen "
                       "depende del radio y el radio del tiempo: se **compone**."),
                ("tex", r"(V\circ r)(t)=V\bigl(r(t)\bigr)=\frac{4}{3}\pi(2t)^{3}=\frac{4}{3}\pi\cdot 8t^{3}=\frac{32}{3}\pi t^{3}"),
                ("err", "Error frecuente: escribir $\\tfrac43\\pi\\cdot2t^{3}$. El cubo afecta a **todo** "
                        "el paréntesis: $(2t)^{3}=8t^{3}$, no $2t^{3}$."),
                ("md", "**(c)** Se plantea la ecuación:"),
                ("tex", r"\frac{32}{3}\pi t^{3}=288\pi \;\Longrightarrow\; t^{3}=\frac{288\cdot 3}{32}=27"),
                ("tex", r"t=\sqrt[3]{27}=3\ \text{s}"),
                ("md", "**Verificación:** a los 3 s el radio es $r=6$ cm, y "
                       "$V=\\tfrac43\\pi(216)=288\\pi$ ✓"),
                ("info", "Nótese la estructura: (b) es una **composición** y (c) es en el fondo una "
                         "**inversa** ($t$ dado $V$). Las dos herramientas de la pestaña 4 aparecen "
                         "juntas en un modelo real."),
            ],
        },
    ]
    mostrar_ejercicios(ejercicios_u6, abrir_todo)


# ==================================================================================
# TAB 7 — ERRORES FRECUENTES
# ==================================================================================
with TABS[7]:
    st.header("⚠️ Errores frecuentes y advertencias sobre el material")

    st.subheader("Dos correcciones a la presentación de la unidad")
    st.error(
        "**Diapositiva 24 — Ejercicio 2, $g(x)=\\dfrac{1}{x^{2}-1}$.**\n\n"
        "El análisis del rango tiene los dos últimos incisos invertidos. Con "
        "$x^{2}=1+\\tfrac1y$:\n\n"
        "• Si $-1<y<0$, entonces $\\tfrac1y<-1$ y $1+\\tfrac1y<0$: **no** hay solución.\n\n"
        "• Si $y\\le-1$, entonces $-1\\le\\tfrac1y<0$ y $1+\\tfrac1y\\ge0$: **sí** hay solución.\n\n"
        "El resultado final $\\operatorname{Ran}(g)=(-\\infty,-1]\\cup(0,+\\infty)$ **sí** es "
        "correcto; lo que está mal es el razonamiento intermedio, que contradice la conclusión."
    )
    st.error(
        "**Diapositiva 60(b) — $f(x)=\\dfrac{2x+1}{x-3}$.**\n\n"
        "La inversa $f^{-1}(x)=\\dfrac{3x+1}{x-2}$ está bien despejada, pero la nota de que «esta "
        "función es su propia inversa» es falsa: $f(f(x))=\\dfrac{5x-1}{10-x}\\neq x$. "
        "Sólo comparte la **forma** $\\dfrac{ax+b}{cx+d}$, que es común a toda la familia de "
        "homografías. Ver el ejercicio 4 de la pestaña de Composición e inversa."
    )

    st.markdown("---")
    st.subheader("Catálogo de errores de los alumnos")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("##### Álgebra de funciones")
        st.markdown(
            """
| Se escribe | Lo correcto |
|---|---|
| $f(a+b)=f(a)+f(b)$ | falso en general |
| $f(2x)=2f(x)$ | falso; si $f=x^2$, $f(2x)=4f(x)$ |
| $f^{-1}(x)=\\dfrac{1}{f(x)}$ | son cosas distintas |
| $\\sqrt{a+b}=\\sqrt a+\\sqrt b$ | falso |
| $(a+b)^2=a^2+b^2$ | falta $2ab$ |
| $-3^2=9$ | $-3^2=-9$; $(-3)^2=9$ |
"""
        )
        st.markdown("##### Dominios")
        st.markdown(
            """
- Aplicar «radicando $\\ge0$» a raíces de índice **impar**: no aplica.
- Olvidar que raíz **en el denominador** exige $>0$ estricto, no $\\ge0$.
- **Unir** restricciones en vez de **intersecarlas**.
- Simplificar primero y calcular el dominio después: las restricciones se pierden.
  ($\\left(\\sqrt{x+1}\\right)^{2}=x+1$ **sólo** para $x\\ge-1$.)
- Creer que los ceros del **numerador** restringen el dominio.
"""
        )
    with c2:
        st.markdown("##### Propiedades e inversas")
        st.markdown(
            """
- Decir que una fórmula «es inyectiva» sin mencionar dominio y codominio.
- Probar suprayectividad sin **verificar** que el $x$ construido esté en el dominio.
- Refutar $\\forall$ con palabras en vez de un contraejemplo concreto.
- Al despejar la inversa de una cuadrática restringida, **olvidar elegir el signo**
  de la raíz según el dominio.
- No declarar $\\operatorname{Dom}(f^{-1})=\\operatorname{Ran}(f)$.
"""
        )
        st.markdown("##### Modelos")
        st.markdown(
            """
- Usar el dominio algebraico en lugar del **físico**.
- No descartar raíces sin sentido (tiempos o longitudes negativas).
- Mezclar unidades (pies con millas, minutos con segundos).
- Dar el resultado sin unidades ni interpretación.
- No verificar la continuidad en las fronteras de un modelo por tramos.
"""
        )

    st.markdown("---")
    st.subheader("Checklist para el pizarrón")
    st.success(
        "**Antes de dar por terminado un ejercicio, preguntar al grupo:**\n\n"
        "1. ¿Escribí el **dominio** del resultado, no sólo la fórmula?\n\n"
        "2. ¿**Verifiqué** con un valor numérico concreto?\n\n"
        "3. Si hubo una restricción al inicio, ¿**sobrevivió** a la simplificación?\n\n"
        "4. ¿La respuesta tiene **sentido** (signo, magnitud, unidades)?\n\n"
        "5. Si descarté una solución, ¿**expliqué por qué**?"
    )

    st.markdown("---")
    st.caption(
        "Ejercicios tomados de Stewart, *Precálculo*, Cap. 2 (§2.1, pp. 142–152; §2.2, pp. 152–156) "
        "y de la presentación de la Unidad 1 del curso. Las referencias con número de ejercicio y "
        "página corresponden a las páginas verificadas del libro; el resto se cita por diapositiva."
    )
