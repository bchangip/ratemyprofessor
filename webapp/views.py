# -*- coding: utf-8 -*-
# universidad del Valle de Guatemala
from __future__ import division
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import registration.signals
from .models import EmailForm
from django.forms import modelformset_factory
import time
import socket

# HOST = "172.20.10.6"
# HOST = "74.125.206.26"
HOST = "127.0.0.1"
PORT = 2407
# PORT = 25

def createEmailPage(request):
	if(request.method == 'GET'):
		return render(
			request, 
			'webapp/createEmail.html',
			{
				'createEmailForm': EmailForm()
			}
		)
	else:
		try:
			newEmail = EmailForm(request.POST)
			sleep_time = 0.1
			if newEmail.is_valid():
				print(newEmail.cleaned_data['fromEmail'])
				print(newEmail.cleaned_data['toEmail'])
				print(newEmail.cleaned_data['data'])

				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((HOST, PORT))
				data = s.recv(1024)
				print('Received', repr(data))
				s.sendall(b'HELO uvg.mail')
				time.sleep(sleep_time)
				data = s.recv(1024)
				print('Received', repr(data))

				#MAIL FROM
				command = "MAIL FROM: <" + str(newEmail.cleaned_data['fromEmail']) + ">"
				# print (command)
				s.sendall(command.encode())
				time.sleep(sleep_time)
				data = s.recv(1024)
				print('Received', repr(data))
				#RCPT TO
				# print (newEmail.cleaned_data['toEmail'].split(','))
				for mail in newEmail.cleaned_data['toEmail'].split(','):
					print (mail)
					s.sendall(("RCPT TO: <" + mail + ">").encode())
					time.sleep(sleep_time)
					data = s.recv(1024)
					print('Received', repr(data))
				#DATA
				msgData = str(newEmail.cleaned_data['data'])
				s.sendall(b'DATA')
				time.sleep(sleep_time)
				data = s.recv(1024)
				print('Received', repr(data))
				# Send message.
				s.sendall(msgData.encode())
				time.sleep(sleep_time)
				#. (Enviar .)
				s.sendall(b'.')
				time.sleep(sleep_time)
				data = s.recv(1024)
				print('Received', repr(data))
				#QUIT
				s.sendall(b'QUIT')
				time.sleep(sleep_time)
				data = s.recv(1024)
				print('Received', repr(data))
				s.close() # Este close no se si va a ser necesario, porque el server cierra la conexion
		except:
			s.close()

		return render(
			request, 
			'webapp/createEmail.html',
			{
				'createEmailForm': EmailForm()
			}
		)

