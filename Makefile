default: build
.PHONY: build

destroy:
	vagrant destroy -f

create: destroy
	vagrant up 
	molecule prepare --force 

