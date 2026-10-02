class CampioneDNA:
    
    def __init__(self,__codice_campione,__sequenza,laboratorio,__geni_mappati=[],__mutazioni_rilevate={}):
        """
        Inizializza tutti gli attributi:
        codice_campione(str): identificativo univoco del campione
        sequenza(str): sequenza nucleotidica
        laboratorio(str): nome del laboratorio di provenienza
        geni_mappati(list): lista che contiene i nomi dei geni identificati nella sequenza
        mutazioni_rilevate(dict): dizionario che associa alla posizione numerica il tipo di mutazione riscontrata  
        """
        self.__codice_campione=__codice_campione
        self.__sequenza=__sequenza.upper()
        self.__geni_mappati=__geni_mappati
        self.__mutazioni_rilevate=__mutazioni_rilevate
        self.laboratorio=laboratorio
        
    def aggiungi_gene(self,nome_gene):
        """
        Aggiunge un nuovo gene alla lista se non è già presente:
        nome_gen(str): nome del gene da aggiungere
        boolean: True se il gene era già presente, False se il gene è stato aggiunto
        """
        if nome_gene in self.__geni_mappati:
            return True
        else:
            self.__geni_mappati.append(nome_gene)
            return False
        
    def registra_mutazione(self,posizione,tipo_mutazione):
        """
        Inserisce o aggiorna una mutazione nel dizionario:
        posizione(int): posizione della mutazione nella sequenza
        tipo_mutazione(str): tipo di mutazione riscontrata
        """
        self.__mutazioni_rilevate[posizione]=tipo_mutazione
        
    def calcola_percentuale_gc(self):
        """
        Calcola e restituisce la percentuale di basi "G" e "C" rispetto alla lunghezza totale della sequenza:
        float: percentuale di "GC" calcolata
        """
        totale_g=self.__sequenza.count("G")
        totale_c=self.__sequenza.count("C")
        totale_gc=totale_g+totale_c
        lunghezza_sequenza=len(self.__sequenza)
        percentuale=(totale_gc/lunghezza_sequenza)*100
        return percentuale

    def stampa_report(self):
        """
        Stampa a schermo una scheda riassuntiva con tutti i dati del campione
        """
        print("REPORT CAMPIONE DNA")
        print("Codice Campione:", self.__codice_campione)
        print("Sequenza:", self.__sequenza)
        print("Laboratorio:", self.laboratorio)
        print("Geni Mappati:", self.__geni_mappati)
        print("Mutazioni Rilevate:", self.__mutazioni_rilevate)
        print("Percentuale GC:", self.calcola_percentuale_gc(), "%")

if __name__=="__main__":
    campione_test=CampioneDNA("DNA-101","atcggcta","LabGen-BioApp")
    lista_geni=["geneA", "ampR", "lacZ"]
    dizionario_mutazioni={45:"sostituzione", 120:"delezione"}
    campione_test.aggiungi_gene("geneA")
    campione_test.registra_mutazione(45,"sostituzione")
    campione_test.calcola_percentuale_gc()
    campione_test.stampa_report()
    



        
        
