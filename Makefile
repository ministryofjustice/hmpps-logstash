default: build
.PHONY: build

destroy:
	vagrant destroy -f


prepare:
	molecule prepare --force 

create: destroy
	vagrant up 
	molecule prepare --force 

