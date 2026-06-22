import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lines 122-177 (0-indexed: 121-176) are the old services section
new_services = """  <!-- ══════════════ SERVICES ══════════════ -->
  <section id="services" class="section">
    <div class="container">
      <div class="services-header fade-up">
        <div>
          <span class="section-label">Lo que ofrecemos</span>
          <h2 class="section-title">Servicios <span class="highlight">profesionales</span></h2>
          <p class="section-subtitle">Soluciones aéreas a medida para cada proyecto, con equipos de última generación y total cobertura de seguro.</p>
        </div>
        <a href="#contact" class="btn btn-outline services-header-cta">Solicitar presupuesto</a>
      </div>

      <!-- 2 tarjetas destacadas -->
      <div class="services-featured fade-up">

        <div class="svc-card svc-card--featured">
          <div class="svc-card-num">01</div>
          <div class="svc-card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9.5L12 3l9 6.5V20a1 1 0 01-1 1H4a1 1 0 01-1-1V9.5z"/>
              <path d="M9 21V12h6v9"/>
            </svg>
          </div>
          <span class="svc-card-tag">Más solicitado</span>
          <h3 class="svc-card-title">Fotografía Inmobiliaria</h3>
          <p class="svc-card-desc">Imágenes aéreas que destacan propiedades y urbanizaciones, aumentando su atractivo y valor de venta en portales inmobiliarios.</p>
          <ul class="svc-card-features">
            <li><span class="svc-check">✓</span> Fotos 4K ultra definición</li>
            <li><span class="svc-check">✓</span> Vídeo cinematográfico</li>
            <li><span class="svc-check">✓</span> Entrega en 48 h</li>
          </ul>
          <a href="#contact" class="svc-card-link">Solicitar presupuesto <span>→</span></a>
        </div>

        <div class="svc-card svc-card--featured">
          <div class="svc-card-num">02</div>
          <div class="svc-card-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="7" width="15" height="10" rx="2"/>
              <path d="M17 9.5l5-2.5v10l-5-2.5V9.5z"/>
            </svg>
          </div>
          <span class="svc-card-tag">Cinematográfico</span>
          <h3 class="svc-card-title">Producción Audiovisual</h3>
          <p class="svc-card-desc">Vídeos aéreos de cine para publicidad, series, cortometrajes y contenido de marca. Planos imposibles desde el aire.</p>
          <ul class="svc-card-features">
            <li><span class="svc-check">✓</span> Grabación RAW 4K/6K</li>
            <li><span class="svc-check">✓</span> Edición profesional</li>
            <li><span class="svc-check">✓</span> Música y color grading</li>
          </ul>
          <a href="#contact" class="svc-card-link">Solicitar presupuesto <span>→</span></a>
        </div>

      </div>

      <!-- 4 tarjetas secundarias -->
      <div class="services-grid-4 fade-up">

        <div class="svc-card svc-card--small">
          <div class="svc-card-num">03</div>
          <div class="svc-card-icon svc-card-icon--sm">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>
            </svg>
          </div>
          <h3 class="svc-card-title">Eventos &amp; Bodas</h3>
          <p class="svc-card-desc">Captura los momentos únicos de tu celebración desde perspectivas irrepetibles e impactantes.</p>
          <a href="#contact" class="svc-card-link">Más info <span>→</span></a>
        </div>

        <div class="svc-card svc-card--small">
          <div class="svc-card-num">04</div>
          <div class="svc-card-icon svc-card-icon--sm">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="3" width="20" height="14" rx="2"/>
              <path d="M8 21h8M12 17v4"/>
              <path d="M7 8h2v5H7zm4-2h2v7h-2zm4 3h2v4h-2z"/>
            </svg>
          </div>
          <h3 class="svc-card-title">Inspección Industrial</h3>
          <p class="svc-card-desc">Inspección técnica de infraestructuras, torres, tejados y plantas industriales con total seguridad.</p>
          <a href="#contact" class="svc-card-link">Más info <span>→</span></a>
        </div>

        <div class="svc-card svc-card--small">
          <div class="svc-card-num">05</div>
          <div class="svc-card-icon svc-card-icon--sm">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 20l5-10 4 6 3-4 6 8H3z"/>
              <circle cx="17" cy="5" r="2"/>
            </svg>
          </div>
          <h3 class="svc-card-title">Cartografía &amp; Topografía</h3>
          <p class="svc-card-desc">Levantamientos topográficos, modelos 3D y ortofotografías de alta precisión para ingeniería.</p>
          <a href="#contact" class="svc-card-link">Más info <span>→</span></a>
        </div>

        <div class="svc-card svc-card--small">
          <div class="svc-card-num">06</div>
          <div class="svc-card-icon svc-card-icon--sm">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M14 14.76V3.5a2.5 2.5 0 00-5 0v11.26a4.5 4.5 0 105 0z"/>
            </svg>
          </div>
          <h3 class="svc-card-title">Análisis &amp; Termografía</h3>
          <p class="svc-card-desc">Detección de pérdidas térmicas y diagnóstico de cubiertas solares con cámara térmica.</p>
          <a href="#contact" class="svc-card-link">Más info <span>→</span></a>
        </div>

      </div>
    </div>
  </section>
"""

# Replace lines 122-177 (1-indexed) = indices 121-176 (0-indexed)
new_lines = lines[:121] + [new_services] + lines[177:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("SUCCESS: Services section replaced")
