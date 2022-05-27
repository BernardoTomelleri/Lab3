% Acquisire i dati utilizzando la funzionalita 'Protocol' di Waveforms
% con i seguenti settaggi:
% SPI
% Select: None
% Frequency 50 kHz (la stessa del clock del flip-flop)
% DQ0: DIO 1 (ingresso su cui avete i dati, ovvero l'uscita del flip-flop)
% Clock: DIO 0 (ingresso su cui avete collegato il clock del flip-flop)
% Selezionare i dati in formato 'Decimal' dalla 'rotellina' in alto a dx
% Spy
% Mode: Three-wire
% Data bits: 8
% Prendere pochi dati, un secondo o meno, clickando su Receive e subito
% dopo su Stop
% Salvare i dati clickando sull'icona del dischetto
% Editare il file per rimuovere il "Data: " iniziale.
close all;
clear all;
myData=load('default.txt');
nbit=8;
myDataBin=dec2bin(myData,nbit);
sz_myData=size(myDataBin);
myStream=zeros((nbit-1)*(sz_myData(1)+1),1);
for i=1:sz_myData(1)-1
    for j=1:nbit
        myStream(1+(i-1)*nbit+j-1)=str2double(myDataBin(i,j));
    end
end
dr=1/50e3; % Clock period
ttime=0:dr:(length(myStream)-1)*dr;
clear ma1;
ma1=movmean(myStream,8);
ma1(end-nbit+1:end)=[];
ttime1=ttime(1:end-nbit);
figure(2);
clf;
plot(ttime1,ma1);
title('First Moving Average')
xlabel('Time (s)');
ylabel('A.U.');
clear ma2;
ma2=movmean(ma1,8);
ma2(end-nbit+1:end)=[];
ttime2=ttime1(1:end-nbit);
%remove mean value to simplify fit
ma2z=ma2-mean(ma2);
figure(3);
clf;
plot(ttime2',ma2)
title('Second Moving Average')
xlabel('Time (s)');
ylabel('A.U.');
clear ma3;
ma3=movmean(ma2,8);
ma3(end-nbit+1:end)=[];
ttime3=ttime2(1:end-nbit);
%remove mean value to simplify fit
ma3z=ma3-mean(ma3);
figure(4);
clf;
plot(ttime3,ma3)
title('Third Moving Average')
xlabel('Time (s)');
ylabel('A.U.');
[fitresult, gof] = createFit(ttime3', ma3z)
ma3zD=downsample(ma3z,8);
ttimeD=downsample(ttime3,8);
[fitresultD, gofD] = createFit(ttimeD', ma3zD)
residuals=ma3zD-fitresultD(ttimeD');
rmsNoise=std(residuals);
rmsSigMax=0.5*sqrt(2)/2;
snrmax=rmsSigMax^2/rmsNoise^2;
enob=(10*log10(snrmax)-1.76)/6.02;

fprintf('This ADC is equivalent to an ideal ADC with:\n\tENOB = %g\n\tSamplig Frequency %g SPS\n', enob,1/dr/8);
