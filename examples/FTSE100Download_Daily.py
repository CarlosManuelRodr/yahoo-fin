from yahoo_fin import stock_info as si
from tqdm import tqdm
from datetime import date
import os

tickers = ['AAL.L',
 'ABF.L',
 'ADM.L',
 'AHT.L',
 'ANTO.L',
 'AUTO.L',
 'AV.L',
 'AVST.L',
 'AVV.L',
 'AZN.L',
 'BA.L',
 'BARC.L',
 'BATS.L',
 'BDEV.L',
 'BHP.L',
 'BKG.L',
 'BLND.L',
 'BME.L',
 'BNZL.L',
 'BP.L',
 'BRBY.L',
 'BT-A.L',
 'CCH.L',
 'CPG.L',
 'CRDA.L',
 'CRH.L',
 'DCC.L',
 'DGE.L',
 'EVR.L',
 'EXPN.L',
 'FERG.L',
 'FLTR.L',
 'FRES.L',
 'GLEN.L',
 'GSK.L',
 'GVC.L',
 'HIK.L',
 'HL.L',
 'HLMA.L',
 'HSBA.L',
 'HSV.L',
 'IAG.L',
 'ICP.L',
 'IHG.L',
 'III.L',
 'IMB.L',
 'INF.L',
 'ITRK.L',
 'JD.L',
 'JET.L',
 'JMAT.L',
 'KGF.L',
 'LAND.L',
 'LGEN.L',
 'LLOY.L',
 'LSE.L',
 'MNDI.L',
 'MNG.L',
 'MRO.L',
 'MRW.L',
 'NG.L',
 'NWG.L',
 'NXT.L',
 'OCDO.L',
 'PHNX.L',
 'PNN.L',
 'POLY.L',
 'PRU.L',
 'PSN.L',
 'PSON.L',
 'RB.L',
 'RDSA.L',
 'REL.L',
 'RIO.L',
 'RMV.L',
 'RR.L',
 'RSA.L',
 'RTO.L',
 'SBRY.L',
 'SDR.L',
 'SGE.L',
 'SGRO.L',
 'SKG.L',
 'SLA.L',
 'SMDS.L',
 'SMIN.L',
 'SMT.L',
 'SN.L',
 'SPX.L',
 'SSE.L',
 'STAN.L',
 'STJ.L',
 'SVT.L',
 'TSCO.L',
 'TW.L',
 'ULVR.L',
 'UU.L',
 'VOD.L',
 'WPP.L',
 'WTB.L']
                
print("Downloading tickers...")

pbar = tqdm(total=len(tickers))

def get_intraday_data_from_ticker(ticker):
    pbar.update(1)
    return si.get_data(ticker, interval='1d', index_as_date=False)


result = list(map(lambda ticker: get_intraday_data_from_ticker(ticker), tickers))

if not os.path.exists('FTSE100'):
    os.makedirs('FTSE100')

if not os.path.exists('FTSE100/'):
    os.makedirs('FTSE100/')
for i in range(len(tickers)):
    f = open('FTSE100/' + tickers[i] + ".csv", "w+")
    if not result[i].empty:
        f.write(result[i].drop(columns=['ticker']).to_csv(index=False))
    else:
        f.write("Failed")
    f.close()
    
print("Done!")
