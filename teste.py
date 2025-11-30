##from app import app, db, FichaTecnica

##with app.app_context():
  ##  fichas = FichaTecnica.query.all()
    ##for f in fichas:
      ##  print(f.id, f.descricao, f.tipo_espuma_id)

    ##print("Total de fichas:", FichaTecnica.query.count())

from app import app, db, FichaTecnica, FichaTecnicaComponente, Componente

with app.app_context():
    fichas = FichaTecnica.query.all()

    for f in fichas:
        print(f"\nFicha:", f.id, "-", f.descricao)

        # busca os vínculos
        vinculos = FichaTecnicaComponente.query.filter_by(ficha_tecnica_id=f.id).all()

        # percorre cada vínculo e mostra o componente
        for v in vinculos:
            comp = Componente.query.get(v.componente_id)
            print("   Componente:", comp.id, comp.nome)

    print("\nTotal de fichas:", FichaTecnica.query.count())
