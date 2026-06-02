# CRM Verticales - Venezuela
## Módulos personalizados para Odoo 18.0

Suite de cuatro módulos que extienden el CRM nativo de Odoo con verticales especializadas y localización venezolana.

**Autor:** Eduardo Álvarez — En3D Tecnología C.A.
**Licencia:** LGPLv3
**Versión Odoo:** 18.0

---

## Módulos incluidos

### 1. `l10n_ve_crm` — Localización Venezolana del CRM
Módulo base que todos los verticales usan como dependencia.

- Campos de identificación: tipo de documento (V/E/J/G/P) + número
- Validación automática de RIF y cédulas
- 24 estados de Venezuela pre-cargados
- Doble moneda: monto en USD + tasa BCV → conversión automática a Bs

### 2. `crm_funeraria` — CRM para Funerarias
Vertical especializada en servicios exequiales.

**Casos de uso:**
- Servicios prevenidos (planes a futuro con financiamiento)
- Necesidad inmediata (con campo de urgencia 🔴🟡🟢)
- Traslados nacionales e internacionales

**Modelos nuevos:**
- `crm.funeraria.plan` — Planes funerarios con servicios incluidos
- `crm.funeraria.cementerio` — Catálogo de cementerios/crematorios

**Campos clave en oportunidades:**
- Datos del fallecido (sólo si modalidad = necesidad inmediata)
- Familiar responsable con parentesco
- Fechas de velatorio y sepelio
- Documentación (acta, permisos)
- Cementerio destino

**Pipeline:** Contacto → Cotización → Negociación → Servicio en Curso → Completado

### 3. `crm_autopartes` — CRM para Venta de Repuestos
Vertical para talleres, distribuidores y venta directa de autopartes.

**Modelos nuevos:**
- `autopartes.vehiculo` — Ficha del vehículo (VIN, placa, motor, kilometraje)
- `autopartes.pieza` — Catálogo de piezas con códigos OEM/equivalentes
- `autopartes.pieza.solicitada` — Líneas de piezas en cada oportunidad

**Tipos de cliente:** B2C, Taller, Flota, Mayorista, Concesionario

**Origen de repuesto:** OEM, Aftermarket, Usado, Remanufacturado

**Pipeline:** Consulta → Verificando Disponibilidad → Cotización → Orden → Entrega

### 4. `crm_calzado` — CRM para Retail de Calzado
Diseñado pensando en el caso Sport Market (Nike, Skechers, Under Armour, On Running).

**Modelos nuevos:**
- `calzado.marca` — Catálogo de marcas (7 marcas pre-cargadas)
- `calzado.modelo` — Modelos por marca con vista Kanban con imágenes

**Campos clave:**
- Categoría deportiva (running, basketball, training, lifestyle, etc.)
- Conversión automática de tallas: largo en cm → US/EU/MX
- Tipo de pisada (neutra/pronadora/supinadora) y arco del pie
- Programa de fidelidad (Bronze → Platinum)
- Sistema de referidos
- **Flag de personalización 3D** (conexión natural con servicios En3D)

**Pipeline:** Interés → Prueba en Tienda → Reserva → Venta Confirmada

---

## Instalación

### Orden obligatorio de instalación

```
1. l10n_ve_crm     (primero, los demás dependen de él)
2. crm_funeraria   (opcional)
3. crm_autopartes  (opcional)
4. crm_calzado     (opcional)
```

Los tres verticales son independientes entre sí — puedes instalar solo el que necesites para cada cliente.

### Pasos

1. **Copia las carpetas** a tu directorio de addons personalizados:
   ```bash
   cp -r l10n_ve_crm crm_funeraria crm_autopartes crm_calzado /opt/odoo/custom-addons/
   ```

2. **Verifica el `addons_path`** en `/etc/odoo/odoo.conf`:
   ```ini
   addons_path = /opt/odoo/addons,/opt/odoo/custom-addons
   ```

3. **Reinicia Odoo:**
   ```bash
   sudo systemctl restart odoo
   ```

4. **En la interfaz web:**
   - Activa el modo desarrollador
   - Apps → Actualizar lista de Apps
   - Quita el filtro "Apps" del buscador
   - Busca e instala los módulos en el orden indicado

---

## Probar antes de producción

**Muy recomendado:** crea una base de datos de prueba primero.

```bash
# Crear DB de prueba
createdb -U odoo crm_test_ve

# Lanzar Odoo apuntando a la DB de prueba
./odoo-bin -d crm_test_ve --addons-path=addons,custom-addons -i l10n_ve_crm,crm_funeraria,crm_autopartes,crm_calzado
```

---

## Personalización adicional sugerida

Para llevar estos módulos a producción real con tus clientes, considera añadir:

1. **Reportes QWeb personalizados** — Cotizaciones con identidad visual del cliente
2. **Automatizaciones** — Recordatorios automáticos, asignación inteligente de leads
3. **Integraciones**:
   - **WhatsApp Business API** (Tridi-style con n8n)
   - **PredixIA** vía API XML-RPC para análisis predictivo
   - **Pasarelas de pago** locales (Mercantil, BNC, Pago Móvil)
4. **Localización fiscal venezolana** — Facturación electrónica SENIAT (módulos OCA)
5. **Multi-empresa** — Si planeas vender el mismo sistema a varios clientes

---

## Próximos pasos sugeridos

1. Probar cada vertical en una DB demo
2. Adaptar las etapas del pipeline al flujo real de cada cliente
3. Cargar el catálogo real (planes funerarios, piezas, modelos)
4. Conectar con PredixIA vía API para análisis predictivo de leads
5. Integrar WhatsApp como canal de captura
6. Reportes y dashboards específicos por vertical

---

## Soporte

Para extender o personalizar cualquiera de estos módulos, los archivos clave son:

- `models/` — Lógica de negocio (Python)
- `views/` — Interfaces de usuario (XML)
- `data/` — Datos pre-cargados y etapas del pipeline
- `security/` — Permisos de acceso

Buena base para construir verticales adicionales (clínicas, inmobiliarias, restaurantes, etc.).
